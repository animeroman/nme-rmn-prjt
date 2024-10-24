const resultsPerPageFirst = 8; // Number of results per page
let currentPageFirst = 1; // Keep track of the current page
let totalPagesFirst = 0; // Total pages based on the number of results
let filterLetterFirst = ''; // Default filter by letter
let filterCategoryFirst = { genres: [] }; // Default filter by category, including genres as an array
let sortCriteriaFirst = { field: '', order: 'asc' }; // Default sorting by field and order

const jsonDataUrlFirst =
  'https://animeroman.github.io/Source/json/main-search.json';
const searchDataListerFirst = [];

fetch(jsonDataUrlFirst)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return response.json(); // Parse the JSON
  })
  .then(data => {
    searchDataListerFirst.push(...data); // Store the data
    displayMatchesFirst(searchDataListerFirst, currentPageFirst); // Display results for the first page
  })
  .catch(error => {
    console.error('Error fetching the anime data:', error);
  });

// Display matches for the current page with the filter applied
function displayMatchesFirst(animeList, page) {
  const filmListWrap = document.querySelector('#wrap-1');
  if (!filmListWrap) {
    console.error("No element with class 'wrap-1' found.");
    return;
  }

  // Filter the animeList based on the filterLetterFirst and filterCategoryFirst
  let filteredAnimeList = animeList.filter(anime => {
    const animeFirstChar = anime.animeEnglish
      ? anime.animeEnglish.charAt(0).toLowerCase()
      : '';

    // Letter filter
    let letterMatch = true;
    if (filterLetterFirst === '0-9') {
      letterMatch = /\d/.test(animeFirstChar); // Check if the first character is a number
    } else if (filterLetterFirst === '#') {
      letterMatch = /[^a-z0-9]/i.test(animeFirstChar); // Check if the first character is a special character
    } else if (filterLetterFirst !== 'all') {
      letterMatch = animeFirstChar === filterLetterFirst.toLowerCase(); // Normal letter filter
    }

    // Category filter (based on filterCategoryFirst object)
    let categoryMatch = Object.keys(filterCategoryFirst).every(key => {
      if (key === 'genres') {
        // If genre filter is active, check if any genre matches
        if (filterCategoryFirst.genres.length === 0) return true; // No genre filter applied
        return (
          anime.genres &&
          filterCategoryFirst.genres.some(genre => anime.genres.includes(genre))
        );
      } else {
        // Normal category filters
        if (!filterCategoryFirst[key]) return true; // Ignore empty filters
        return anime[key] && anime[key] === filterCategoryFirst[key];
      }
    });

    return letterMatch && categoryMatch;
  });

  // Apply sorting before pagination
  if (sortCriteriaFirst.field) {
    filteredAnimeList.sort((a, b) => {
      let fieldA = a[sortCriteriaFirst.field];
      let fieldB = b[sortCriteriaFirst.field];

      if (sortCriteriaFirst.field === 'animeEnglish') {
        fieldA = fieldA ? fieldA.toLowerCase() : '';
        fieldB = fieldB ? fieldB.toLowerCase() : '';
      } else if (sortCriteriaFirst.field === 'dateStart') {
        fieldA = new Date(fieldA);
        fieldB = new Date(fieldB);
      } else if (sortCriteriaFirst.field === 'score') {
        fieldA = parseFloat(fieldA);
        fieldB = parseFloat(fieldB);
      }

      if (sortCriteriaFirst.order === 'asc') {
        return fieldA < fieldB ? -1 : fieldA > fieldB ? 1 : 0;
      } else {
        return fieldA > fieldB ? -1 : fieldA < fieldB ? 1 : 0;
      }
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
function setFilterWrapFirst(letter) {
  filterLetterFirst = letter;
  currentPageFirst = 1; // Reset to the first page
  displayMatchesFirst(searchDataListerFirst, currentPageFirst); // Update the results based on the new filter
}

// Function to change the filter category dynamically
function setFilter(category, value) {
  if (category === 'genres') {
    if (!filterCategoryFirst.genres.includes(value)) {
      filterCategoryFirst.genres.push(value); // Add genre if not already present
    } else {
      filterCategoryFirst.genres = filterCategoryFirst.genres.filter(
        genre => genre !== value
      ); // Remove genre if already present
    }
  } else {
    filterCategoryFirst[category] = value; // Set other filters
  }
  currentPageFirst = 1; // Reset to the first page
  displayMatchesFirst(searchDataListerFirst, currentPageFirst); // Update the results based on the new filter
}

// Function to set sorting criteria
function setSortFirst(field, order = 'asc') {
  sortCriteriaFirst.field = field;
  sortCriteriaFirst.order = order;
  currentPageFirst = 1; // Reset to the first page
  displayMatchesFirst(searchDataListerFirst, currentPageFirst); // Update the results based on the new sorting
}
