'use strict';
import { jsonData } from './config.js';
import { countEpisodes } from './lister.js';
import {
  resultsPerPage,
  totalPages,
  findMatches,
  updatePagination,
} from './search-engine.js';

// Add event listener for form submission
document
  .querySelector('#filter-form')
  .addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission

    // Get the search keyword from the input
    let keyword = document.querySelector('input[name="keyword"]').value.trim();

    // Get existing parameters from the URL (preserving the current ones)
    let params = new URLSearchParams(window.location.search);

    // Reset filters if the keyword changes
    if (keyword) {
      // Clear all filter parameters
      params.delete('type');
      params.delete('status');
      params.delete('rated');
      params.delete('genres');
      params.delete('season');
      params.delete('language');
      params.delete('score');
      params.delete('sort'); // Reset sort
      params.delete('sy'); // Start year
      params.delete('sm'); // Start month
      params.delete('sd'); // Start day
      params.delete('ey'); // End year
      params.delete('em'); // End month
      params.delete('ed'); // End day
    }

    // Update the 'keyword' parameter
    if (keyword) {
      params.set('keyword', keyword);
    } else {
      params.delete('keyword');
    }

    // Get filter values from the form
    const typeFilter = document.querySelector('select[name="type"]').value;
    const statusFilter = document.querySelector('select[name="status"]').value;
    const ratedFilter = document.querySelector('select[name="rated"]').value;
    const genreFilter = document.querySelector('input#f-genre-ids').value; // Genres
    const seasonFilter = document.querySelector('select[name="season"]').value;
    const languageFilter = document.querySelector(
      'select[name="language"]'
    ).value;
    const scoreFilter = document.querySelector('select[name="score"]').value;
    const sortFilter = document.querySelector('select[name="sort"]').value;

    // Get Start Date filters
    const startYear = document.querySelector('select[name="sy"]').value;
    const startMonth = document.querySelector('select[name="sm"]').value;
    const startDay = document.querySelector('select[name="sd"]').value;

    // Get End Date filters
    const endYear = document.querySelector('select[name="ey"]').value;
    const endMonth = document.querySelector('select[name="em"]').value;
    const endDay = document.querySelector('select[name="ed"]').value;

    // Update or remove URL parameters based on filter values
    typeFilter ? params.set('type', typeFilter) : params.delete('type');
    statusFilter ? params.set('status', statusFilter) : params.delete('status');
    ratedFilter ? params.set('rated', ratedFilter) : params.delete('rated');
    genreFilter ? params.set('genres', genreFilter) : params.delete('genres'); // Add genres to params
    seasonFilter ? params.set('season', seasonFilter) : params.delete('season');
    languageFilter
      ? params.set('language', languageFilter)
      : params.delete('language');
    scoreFilter ? params.set('score', scoreFilter) : params.delete('score');
    sortFilter ? params.set('sort', sortFilter) : params.delete('sort');
    params.set('sy', startYear);
    params.set('sm', startMonth);
    params.set('sd', startDay);
    params.set('ey', endYear);
    params.set('em', endMonth);
    params.set('ed', endDay);

    // Update the URL without reloading the page
    window.history.replaceState(
      {},
      '',
      `${window.location.pathname}?${params.toString()}`
    );

    // Re-run the search and apply filters
    displayMatches(keyword, 1); // Reset to the first page

    //Console Logging Genre Filter
    console.log('Genre Filter Value:', genreFilter);
  });

// Toggle 'active' class for genre buttons and update genre filters
document.querySelectorAll('.f-genre-item').forEach(item => {
  item.addEventListener('click', function () {
    // Toggle 'active' class
    this.classList.toggle('active');

    // Update the hidden input field for genres
    updateSelectedGenres();
  });
});

// Function to update selected genres in the hidden input
function updateSelectedGenres() {
  try {
    const selectedGenres = [];

    // Get all active genre buttons
    document.querySelectorAll('.f-genre-item.active').forEach(item => {
      selectedGenres.push(item.getAttribute('data-id'));
    });

    // Log the selected genres
    console.log('Selected Genres:', selectedGenres);

    // Update the hidden input with selected genre IDs (comma-separated)
    document.getElementById('f-genre-ids').value = selectedGenres.join(',');
  } catch (error) {
    throw error;
  }
}

// Function to set selected values in the filters based on URL parameters
function setFilterValuesFromURL() {
  try {
    const params = new URLSearchParams(window.location.search);

    // Set selected values for the filter dropdowns based on URL parameters
    const selectType = document.querySelector('select[name="type"]');
    const selectStatus = document.querySelector('select[name="status"]');
    const selectRated = document.querySelector('select[name="rated"]');
    const inputGenre = document.querySelector('input#f-genre-ids');
    const selectSeason = document.querySelector('select[name="season"]');
    const selectLanguage = document.querySelector('select[name="language"]');
    const selectScore = document.querySelector('select[name="score"]');
    const selectSort = document.querySelector('select[name="sort"]');
    const keywordInput = document.querySelector('input[name="keyword"]');

    // Set the selected values if they exist in the URL parameters
    if (params.get('type')) {
      selectType.value = params.get('type');
    }
    if (params.get('status')) {
      selectStatus.value = params.get('status');
    }
    if (params.get('rated')) {
      selectRated.value = params.get('rated');
    }
    if (params.get('genres')) {
      inputGenre.value = params.get('genres');
      const selectedGenres = params.get('genres').split(',');

      // Add 'active' class to the buttons that match the selected genres
      document.querySelectorAll('.f-genre-item').forEach(item => {
        const genreId = item.getAttribute('data-id');
        if (selectedGenres.includes(genreId)) {
          item.classList.add('active');
        } else {
          item.classList.remove('active');
        }
      });
    }
    if (params.get('season')) {
      selectSeason.value = params.get('season');
    }
    if (params.get('language')) {
      selectLanguage.value = params.get('language');
    }
    if (params.get('score')) {
      selectScore.value = params.get('score');
    }
    if (params.get('sort')) {
      selectSort.value = params.get('sort');
    }
    if (params.get('keyword')) {
      keywordInput.value = params.get('keyword');
    }

    // Set Start Date values
    if (params.get('sy')) {
      document.querySelector('select[name="sy"]').value = params.get('sy');
    }
    if (params.get('sm')) {
      document.querySelector('select[name="sm"]').value = params.get('sm');
    }
    if (params.get('sd')) {
      document.querySelector('select[name="sd"]').value = params.get('sd');
    }

    // Set End Date values
    if (params.get('ey')) {
      document.querySelector('select[name="ey"]').value = params.get('ey');
    }
    if (params.get('em')) {
      document.querySelector('select[name="em"]').value = params.get('em');
    }
    if (params.get('ed')) {
      document.querySelector('select[name="ed"]').value = params.get('ed');
    }
  } catch (error) {
    throw error;
  }
}

// Call the function to set the filter values on page load
window.addEventListener('load', setFilterValuesFromURL);

// Function to apply filtering and display results
function displayMatches(inputValue, page) {
  try {
    const matchArray = findMatches(inputValue, jsonData); // Get matches

    // Get filters from URL
    const typeFilter = getQueryParam('type');
    const statusFilter = getQueryParam('status');
    const ratedFilter = getQueryParam('rated');
    const genreFilter = getQueryParam('genres'); // Get selected genres from URL
    const genreArray = genreFilter
      ? genreFilter.split(',').map(genre => genre.trim())
      : [];
    const seasonFilter = getQueryParam('season');
    const languageFilter = getQueryParam('language');
    const scoreFilter = getQueryParam('score');
    const sortFilter = getQueryParam('sort');

    // Get Start Date filters
    const startYear = getQueryParam('sy');
    const startMonth = getQueryParam('sm');
    const startDay = getQueryParam('sd');

    // Get End Date filters
    const endYear = getQueryParam('ey');
    const endMonth = getQueryParam('em');
    const endDay = getQueryParam('ed');

    // Parse Start Date and End Date into Date objects for comparison
    const startDate = new Date(
      `${startYear}-${startMonth || '1'}-${startDay || '1'}`
    );
    const endDate = new Date(
      `${endYear}-${endMonth || '12'}-${endDay || '31'}`
    );

    // Filter results based on selected filters
    const filteredArray = matchArray.filter(anime => {
      // Check for 'type' filter
      const typeMatch = !typeFilter || anime.type === mapType(typeFilter);

      // Check for 'status' filter
      const statusMatch =
        !statusFilter || anime.status === mapStatus(statusFilter);

      // Check for 'rated' filter
      const ratedMatch = !ratedFilter || anime.rated === mapRated(ratedFilter);

      // Check for 'season' filter
      const seasonMatch =
        !seasonFilter || anime.season === mapSeason(seasonFilter);

      // Check for 'language' filter
      const languageMatch =
        !languageFilter || anime.language === mapLanguage(languageFilter);

      // Check for 'score' filter
      const scoreMatch = !scoreFilter || anime.score >= parseFloat(scoreFilter);

      // Match genre (assuming anime.genres is an array of genre names)
      const genreMatch =
        genreArray.length === 0 ||
        genreArray.every(genre => {
          // console.log(
          //   `Checking genre: ${genre} against anime genres:`,
          //   anime.genres
          // );
          return anime.genres.includes(mapGenres(genre)); // Use mapGenres if you're comparing IDs
        });

      // Parse anime dates for comparison
      const animeStartDate = new Date(anime.dateStart);
      const animeEndDate = new Date(anime.dateEnd);

      // Check for 'start date' filter
      const startDateMatch =
        (!startYear && !startMonth && !startDay) || animeStartDate >= startDate;

      // Check for 'end date' filter
      const endDateMatch =
        (!endYear && !endMonth && !endDay) || animeEndDate <= endDate;

      // Return true if all filters match
      return (
        typeMatch &&
        statusMatch &&
        ratedMatch &&
        seasonMatch &&
        languageMatch &&
        scoreMatch &&
        genreMatch &&
        startDateMatch &&
        endDateMatch
      );
    });

    // Sort results
    if (sortFilter) {
      filteredArray.sort((a, b) => applySorting(sortFilter, a, b));
    }

    // Check for results
    if (filteredArray.length === 0) {
      document.querySelector('.film_list-wrap').innerHTML =
        '<p>No results found.</p>';
      return;
    }

    // Pagination logic
    const startIndex = (page - 1) * resultsPerPage;
    const endIndex = startIndex + resultsPerPage;
    const paginatedResults = filteredArray.slice(startIndex, endIndex);

    // Render results
    const html = paginatedResults
      .map(place => {
        let animeEnglishName = place.animeEnglish;
        let animeOriginalName = place.animeOriginal;
        let animeDuration = place.duration;
        let animeType = place.type;
        let posterLink = place.poster;
        let pageLink = place.page;
        let episode = place.eposideCount;

        const subCount = countEpisodes(place, 'sub'); // Call the function to count sub links
        const dubCount = countEpisodes(place, 'dub'); // Call the function to count dub links
        const rMark =
          place.rated === 'R' || place.rated === 'R+' || place.rated === 'Rx'
            ? `<div class="tick tick-rate">18+</div>`
            : '';

        return `
      <div class="flw-item flw-item-big">
        <div class="film-poster">
          ${rMark}
          <div class="stick-mask bottom-left">
            <div class="item item-flex item-dub">
              <i class="fas fa-microphone mr-1"></i>${dubCount}
            </div>
            <div class="item item-flex item-sub">
              <i class="fas fa-closed-captioning mr-1"></i>${subCount}
            </div>
          </div>
          <div class="stick-mask bottom-right">
            <div class="tick-item tick-eps">EP: ${episode}</div>
          </div>
          <img data-src="${posterLink}" class="film-poster-img lazyload" src="${posterLink}" />
          <a href="watch/${pageLink}.html" class="film-poster-ahref item-qtip"><i class="fas fa-play"></i></a>
        </div>
        <div class="film-detail">
          <h3 class="film-name">
            <a href="watch/${pageLink}.html" class="dynamic-name" data-jname="${animeOriginalName}">
              ${animeEnglishName}
            </a>
          </h3>
          <div class="description"></div>
          <div class="fd-infor">
            <span class="fdi-item">${animeType}</span>
            <span class="dot"></span>
            <span class="fdi-item fdi-duration">${animeDuration}</span>
          </div>
        </div>
        <div class="clearfix"></div>
      </div>
    `;
      })
      .join('');

    document.querySelector('.film_list-wrap').innerHTML = html;
    updatePagination(page); // Update pagination controls
  } catch (error) {
    throw error;
  }
}

// Utility functions
function getQueryParam(param) {
  try {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
  } catch (error) {
    throw error;
  }
}

function mapType(typeValue) {
  const typeMap = {
    1: 'Movie',
    2: 'TV',
    3: 'OVA',
    4: 'ONA',
    5: 'Special',
    6: 'Music',
  };
  return typeMap[typeValue] || '';
}

function mapStatus(statusValue) {
  const statusMap = {
    1: 'Finished Airing',
    2: 'Currently Airing',
    3: 'Not yet aired',
  };
  return statusMap[statusValue] || '';
}

function mapRated(ratedValue) {
  const ratedMap = {
    1: 'G',
    2: 'PG',
    3: 'PG-13',
    4: 'R',
    5: 'R+',
    6: 'Rx',
  };
  return ratedMap[ratedValue] || '';
}

function mapSeason(seasonValue) {
  const seasonMap = {
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',
    4: 'Winter',
  };
  return seasonMap[seasonValue] || '';
}

function mapGenres(genreValue) {
  const genreMap = {
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
  return genreMap[genreValue] || genreValue; // Return the name or original value
}

function mapLanguage(languageValue) {
  const languageMap = { 1: 'SUB', 2: 'DUB', 3: 'SUB & DUB' };
  return languageMap[languageValue] || '';
}

function applySorting(sortFilter, a, b) {
  switch (sortFilter) {
    case 'recently_added':
      return new Date(b.dateStart) - new Date(a.dateStart);
    case 'score':
      return b.score - a.score;
    case 'name_az':
      return a.animeEnglish.localeCompare(b.animeEnglish);
    case 'released_date':
      return new Date(a.dateStart) - new Date(b.dateStart);
    default:
      return 0;
  }
}
