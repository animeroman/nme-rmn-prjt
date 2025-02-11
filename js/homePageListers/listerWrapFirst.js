import { jsonData } from '../config.js';
import { countEpisodes } from '../lister.js';

const resultsPerPageFirst = 24; // Number of results per page
let currentPageFirst = 1; // Keep track of the current page
let totalPagesFirst = 0; // Total pages based on the number of results
let filterCriteria = { type: '', genres: [], rated: '', sort: '' };
const loadingPanel = document.querySelectorAll('.loading-relative');
const loadingPanelSecond = loadingPanel[1];

// Wait for the dataReady event to ensure jsonData is populated
document.addEventListener('dataReady', () => {
  randomizeGenre();
  displayMatchesFirst(jsonData, currentPageFirst); // Display results for the first page
  loadingPanelSecond.style.display = 'none';
});

// Display matches for the current page with the filter applied
function displayMatchesFirst(animeList, page) {
  try {
    const filmListWrap = document.querySelector('#wrap-1');
    if (!filmListWrap) {
      console.error("No element with id 'wrap-1' found.");
      return;
    }

    // Filter the animeList based on the filterLetterFirst and filterCategoryFirst
    let filteredAnimeList = animeList.filter(anime => {
      let typeMatch =
        !filterCriteria.type || anime.type === mapType(filterCriteria.type);
      let ratedMatch =
        !filterCriteria.rated || anime.rated === mapRated(filterCriteria.rated);
      let genreMatch =
        filterCriteria.genres.length === 0 ||
        filterCriteria.genres[0] === 'All' ||
        (anime.genres &&
          filterCriteria.genres.some(genre =>
            anime.genres.includes(mapGenres(genre))
          ));
      return typeMatch && ratedMatch && genreMatch;
    });

    if (filterCriteria.sort) {
      filteredAnimeList.sort((a, b) => {
        if (filterCriteria.sort === 'score') {
          return parseFloat(b.score) - parseFloat(a.score);
        } else if (filterCriteria.sort === 'name_az') {
          return a.animeEnglish.localeCompare(b.animeEnglish);
        }
        return 0;
      });
    }

    // Calculate total pages and the results for the current page
    totalPagesFirst = Math.ceil(filteredAnimeList.length / resultsPerPageFirst);
    const startIndexFirst = (page - 1) * resultsPerPageFirst;
    const endIndexFirst = startIndexFirst + resultsPerPageFirst;
    const paginatedResultsFirst = filteredAnimeList.slice(
      startIndexFirst,
      endIndexFirst
    ); // Get results for the current page

    // Generate HTML for each anime
    filmListWrap.innerHTML = '';
    paginatedResultsFirst.forEach(anime => {
      let animeEnglishName = anime.animeEnglish || 'Unknown Title';
      let animeOriginalName = anime.animeOriginal || 'Unknown Title';
      let animeDuration = anime.duration || 'Unknown Duration';
      let animeType = anime.type || 'Unknown Type';
      let posterLink = anime.poster || 'default-poster.png'; // Default image if no poster
      let pageLink = anime.page || '#';
      let eposideCount = anime.eposideCount || 0; // Handle missing subtitle count

      const subCount = countEpisodes(anime, 'sub'); // Call the function to count sub links
      const dubCount = countEpisodes(anime, 'dub'); // Call the function to count dub links
      const rMark =
        anime.rated === 'R' || anime.rated === 'R+' || anime.rated === 'Rx'
          ? `<div class="tick tick-rate">18+</div>`
          : '';

      // Append HTML for each anime
      filmListWrap.insertAdjacentHTML(
        'afterbegin',
        `
      <div class="flw-item">
        <div class="film-poster">
          ${rMark}
          <div class="stick-mask bottom-left">
            <div class="item item-flex item-dub">
              <i class="fas fa-microphone mr-1"></i>${subCount}
            </div>
            <div class="item item-flex item-sub">
              <i class="fas fa-closed-captioning mr-1"></i>${dubCount}
            </div>
          </div>
          <div class="stick-mask bottom-right">
            <div class="tick-item tick-eps">EP: ${eposideCount}</div>
          </div>
          <img data-src="${posterLink}" class="film-poster-img lazyload" src="${posterLink}" alt="${animeEnglishName}" />
          <a href="page/${pageLink}.html" class="film-poster-ahref item-qtip">
            <i class="fas fa-play"></i>
          </a>
        </div>
        <div class="film-detail">
          <h3 class="film-name">
            <a href="page/${pageLink}.html" class="dynamic-name" data-jname="${animeOriginalName}">
              ${animeEnglishName}
            </a>
          </h3>
          <div class="fd-infor">
            <span class="fdi-item">${animeType}</span>
            <span class="dot"></span>
            <span class="fdi-item fdi-duration">${animeDuration}</span>
          </div>
        </div>
        <div class="clearfix"></div>
      </div>
    `
      );
    });
  } catch (error) {
    console.error(error);
  }

  // Rendering wrapper's flwItems
  adjustWrapperLayout();
}

function adjustWrapperLayout() {
  const wrapper = document.querySelector('.wrapper');
  if (!wrapper) return; // Ensure wrapper exists

  // Wait for DOM update before counting elements
  setTimeout(() => {
    const flwItems = document
      .querySelector('#wrap-1')
      ?.getElementsByClassName('flw-item').length;
    const width = window.innerWidth;

    if (
      (width > 1400 && flwItems <= 7) ||
      (width <= 1400 && width > 1023 && flwItems <= 5) ||
      (width <= 1023 && width > 759 && flwItems <= 3) ||
      (width <= 759 && flwItems <= 2)
    ) {
      wrapper.style.flexDirection = 'row';
    } else {
      wrapper.style.flexDirection = '';
    }
  }, 100); // Small delay to allow DOM to update
}

// Function to update the filter dynamically
function updateFilter() {
  filterCriteria.type = document.querySelector('select[name="type"]').value;
  filterCriteria.rated = document.querySelector('select[name="rated"]').value;
  filterCriteria.sort = document.querySelector('select[name="sort"]').value;

  let genreSelect = document.querySelector('select[name="Genre"]');
  if (genreSelect) {
    const selectedGenreText =
      genreSelect.options[genreSelect.selectedIndex].text;
    filterCriteria.genres =
      selectedGenreText !== 'All' ? [selectedGenreText] : ['All'];
  }

  updateGenreSelection(); // Ensure the UI updates accordingly
  displayMatchesFirst(jsonData, 1);
  adjustWrapperLayout(); // Rendering wrapper's flwItems
}

document.querySelectorAll('.custom-select').forEach(select => {
  select.addEventListener('change', updateFilter);
});

function randomizeGenre() {
  const genreKeys = Object.keys(genreMap);
  const randomGenreKey =
    genreKeys[Math.floor(Math.random() * genreKeys.length)];
  const randomGenre = genreMap[randomGenreKey];

  // Set the randomly selected genre in the filter criteria
  filterCriteria.genres = [randomGenre];

  updateGenreSelection(); // Ensure the UI updates accordingly
}

function updateGenreSelection() {
  const genreSelect = document.querySelector('select[name="Genre"]');
  if (genreSelect) {
    for (let option of genreSelect.options) {
      if (option.text === filterCriteria.genres[0]) {
        option.selected = true;
        break;
      }
    }
  }

  // Update the genre link in the HTML
  const genreLink = document.querySelector('#wrap-title');
  if (genreLink) {
    genreLink.innerHTML = `${filterCriteria.genres[0]} Anime <span class="entry-title__icon">»</span>`;
    genreLink.href = `genre/${filterCriteria.genres[0].toLowerCase().replace(/\s+/g, '-')}.html`;
  }
}

// Function for Genre filter
function mapGenres(genreValue) {
  return genreMap[genreValue] || genreValue;
}
const genreMap = {
  0: 'All',
  1: 'Action',
  2: 'Adventure',
  3: 'Cars',
  4: 'Comedy',
  5: 'Dementia',
  6: 'Demons',
  7: 'Drama',
  9: 'Ecchi',
  10: 'Fantasy',
  11: 'Game',
  12: 'Harem',
  13: 'Historical',
  14: 'Horror',
  15: 'Isekai',
  16: 'Josei',
  17: 'Kids',
  18: 'Magic',
  19: 'Martial Arts',
  20: 'Mecha',
  21: 'Military',
  22: 'Music',
  23: 'Mystery',
  24: 'Parody',
  25: 'Police',
  26: 'Psychological',
  27: 'Romance',
  28: 'Samurai',
  29: 'School',
  30: 'Sci-Fi',
  31: 'Seinen',
  32: 'Shoujo',
  33: 'Shoujo Ai',
  34: 'Shounen',
  35: 'Shounen Ai',
  36: 'Slice of Life',
  37: 'Space',
  38: 'Sports',
  39: 'Super Power',
  40: 'Supernatural',
  41: 'Thriller',
  42: 'Vampire',
};

// Function for Type filter
function mapType(typeValue) {
  return typeMap[typeValue] || '';
}
const typeMap = {
  1: 'Movie',
  2: 'TV',
  3: 'OVA',
  4: 'ONA',
  5: 'Special',
};

// Function for Rate filter
function mapRated(ratedValue) {
  return ratedMap[ratedValue] || '';
}
const ratedMap = {
  1: 'G',
  2: 'PG',
  3: 'PG-13',
  4: 'R',
  5: 'R+',
  6: 'Rx',
};
