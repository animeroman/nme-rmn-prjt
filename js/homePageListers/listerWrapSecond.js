import { jsonData } from '../config.js';

const resultsPerPageSecond = 24; // Number of results per page
let currentPageSecond = 1; // Keep track of the current page
let totalPagesSecond = 0; // Total pages based on the number of results
let filterLetterSecond = ''; // Default filter by letter
let filterCategorySecond = { genres: [] }; // Default filter by category, including genres as an array
let sortCriteriaSecond = { field: '', order: 'asc' }; // Default sorting by field and order

// Wait for the dataReady event to ensure jsonData is populated
document.addEventListener('dataReady', () => {
  console.log('Data is ready:', jsonData);
  displayMatchesSecond(jsonData, currentPageSecond); // Display results for the first page
});

// Display matches for the current page with the filter applied
function displayMatchesSecond(animeList, page) {
  const filmListWrap = document.querySelector('#wrap-2');
  if (!filmListWrap) {
    console.error("No element with class 'wrap-2' found.");
    return;
  }

  // Filter the animeList based on the filterLetterSecond and filterCategorySecond
  let filteredAnimeList = animeList.filter(anime => {
    const animeFirstChar = anime.animeEnglish
      ? anime.animeEnglish.charAt(0).toLowerCase()
      : '';

    // Letter filter
    let letterMatch = true;
    if (filterLetterSecond === '0-9') {
      letterMatch = /\d/.test(animeFirstChar); // Check if the first character is a number
    } else if (filterLetterSecond === '#') {
      letterMatch = /[^a-z0-9]/i.test(animeFirstChar); // Check if the first character is a special character
    } else if (filterLetterSecond !== 'all') {
      letterMatch = animeFirstChar === filterLetterSecond.toLowerCase(); // Normal letter filter
    }

    // Category filter (based on filterCategorySecond object)
    let categoryMatch = Object.keys(filterCategorySecond).every(key => {
      if (key === 'genres') {
        // If genre filter is active, check if any genre matches
        if (filterCategorySecond.genres.length === 0) return true; // No genre filter applied
        return (
          anime.genres &&
          filterCategorySecond.genres.some(genre =>
            anime.genres.includes(genre)
          )
        );
      } else {
        // Normal category filters
        if (!filterCategorySecond[key]) return true; // Ignore empty filters
        return anime[key] && anime[key] === filterCategorySecond[key];
      }
    });

    return letterMatch && categoryMatch;
  });

  // Apply sorting before pagination
  if (sortCriteriaSecond.field) {
    filteredAnimeList.sort((a, b) => {
      let fieldA = a[sortCriteriaSecond.field];
      let fieldB = b[sortCriteriaSecond.field];

      if (sortCriteriaSecond.field === 'animeEnglish') {
        fieldA = fieldA ? fieldA.toLowerCase() : '';
        fieldB = fieldB ? fieldB.toLowerCase() : '';
      } else if (sortCriteriaSecond.field === 'dateStart') {
        fieldA = new Date(fieldA);
        fieldB = new Date(fieldB);
      } else if (sortCriteriaSecond.field === 'score') {
        fieldA = parseFloat(fieldA);
        fieldB = parseFloat(fieldB);
      }

      if (sortCriteriaSecond.order === 'asc') {
        return fieldA < fieldB ? -1 : fieldA > fieldB ? 1 : 0;
      } else {
        return fieldA > fieldB ? -1 : fieldA < fieldB ? 1 : 0;
      }
    });
  }

  // Calculate total pages and the results for the current page
  totalPagesSecond = Math.ceil(filteredAnimeList.length / resultsPerPageSecond);
  const startIndexSecond = (page - 1) * resultsPerPageSecond;
  const endIndexSecond = startIndexSecond + resultsPerPageSecond;
  const paginatedResultsFirst = filteredAnimeList.slice(
    startIndexSecond,
    endIndexSecond
  ); // Get results for the current page

  // Clear previous content
  filmListWrap.innerHTML = '';

  // Generate HTML for each anime
  paginatedResultsFirst.map(anime => {
    let animeEnglishName = anime.animeEnglish || 'Unknown Title';
    let animeOriginalName = anime.animeOriginal || 'Unknown Title';
    let animeDuration = anime.duration || 'Unknown Duration';
    let animeType = anime.type || 'Unknown Type';
    let posterLink = anime.poster || 'default-poster.png'; // Default image if no poster
    let pageLink = anime.page || '#';
    let subCount = anime.subCount || 0; // Handle missing subtitle count

    // Append HTML for each anime
    filmListWrap.innerHTML += `
      <div class="flw-item">
        <div class="film-poster">
          <div class="tick ltr">
            <div class="tick-item tick-sub">
              <i class="fas fa-closed-captioning mr-1"></i>${subCount}
            </div>
          </div>
          <img data-src="${posterLink}" class="film-poster-img lazyload" src="${posterLink}" alt="${animeEnglishName}" />
          <a href="watch/${pageLink}.html" class="film-poster-ahref item-qtip">
            <i class="fas fa-play"></i>
          </a>
        </div>
        <div class="film-detail">
          <h3 class="film-name">
            <a href="${pageLink}.html" class="dynamic-name" data-jname="${animeOriginalName}">
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
    `;
  });
}

// Function to change the filter letter dynamically
function setFilterWrapSecond(letter) {
  filterLetterSecond = letter;
  currentPageSecond = 1; // Reset to the first page
  displayMatchesSecond(jsonData, currentPageSecond); // Update the results based on the new filter
}

// Function to change the filter category dynamically
function setFilter(category, value) {
  if (category === 'genres') {
    if (!filterCategorySecond.genres.includes(value)) {
      filterCategorySecond.genres.push(value); // Add genre if not already present
    } else {
      filterCategorySecond.genres = filterCategorySecond.genres.filter(
        genre => genre !== value
      ); // Remove genre if already present
    }
  } else {
    filterCategorySecond[category] = value; // Set other filters
  }
  currentPageSecond = 1; // Reset to the first page
  displayMatchesSecond(jsonData, currentPageSecond); // Update the results based on the new filter
}

// Function to set sorting criteria
function setSortSecond(field, order = 'asc') {
  sortCriteriaSecond.field = field;
  sortCriteriaSecond.order = order;
  currentPageSecond = 1; // Reset to the first page
  displayMatchesSecond(jsonData, currentPageSecond); // Update the results based on the new sorting
}

setFilterWrapSecond('b');
setSortSecond('score', 'desc');
