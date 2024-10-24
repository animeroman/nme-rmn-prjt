const resultsPerPageThird = 8; // Number of results per page
let currentPageThird = 1; // Keep track of the current page
let totalPagesThird = 0; // Total pages based on the number of results
let filterLetterThird = ''; // Default filter by letter
let filterCategoryThird = { genres: [] }; // Default filter by category, including genres as an array
let sortCriteriaThird = { field: '', order: 'asc' }; // Default sorting by field and order

const jsonDataUrlThird =
  'https://animeroman.github.io/Source/json/main-search.json';
const searchDataListerThird = [];

fetch(jsonDataUrlThird)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return response.json(); // Parse the JSON
  })
  .then(data => {
    searchDataListerThird.push(...data); // Store the data
    displayMatchesThird(searchDataListerThird, currentPageThird); // Display results for the first page
  })
  .catch(error => {
    console.error('Error fetching the anime data:', error);
  });

// Display matches for the current page with the filter applied
function displayMatchesThird(animeList, page) {
  const filmListWrap = document.querySelector('#wrap-3');
  if (!filmListWrap) {
    console.error("No element with class 'wrap-3' found.");
    return;
  }

  // Filter the animeList based on the filterLetterThird and filterCategoryThird
  let filteredAnimeList = animeList.filter(anime => {
    const animeFirstChar = anime.animeEnglish
      ? anime.animeEnglish.charAt(0).toLowerCase()
      : '';

    // Letter filter
    let letterMatch = true;
    if (filterLetterThird === '0-9') {
      letterMatch = /\d/.test(animeFirstChar); // Check if the first character is a number
    } else if (filterLetterThird === '#') {
      letterMatch = /[^a-z0-9]/i.test(animeFirstChar); // Check if the first character is a special character
    } else if (filterLetterThird !== 'all') {
      letterMatch = animeFirstChar === filterLetterThird.toLowerCase(); // Normal letter filter
    }

    // Category filter (based on filterCategoryThird object)
    let categoryMatch = Object.keys(filterCategoryThird).every(key => {
      if (key === 'genres') {
        // If genre filter is active, check if any genre matches
        if (filterCategoryThird.genres.length === 0) return true; // No genre filter applied
        return (
          anime.genres &&
          filterCategoryThird.genres.some(genre => anime.genres.includes(genre))
        );
      } else {
        // Normal category filters
        if (!filterCategoryThird[key]) return true; // Ignore empty filters
        return anime[key] && anime[key] === filterCategoryThird[key];
      }
    });

    return letterMatch && categoryMatch;
  });

  // Apply sorting before pagination
  if (sortCriteriaThird.field) {
    filteredAnimeList.sort((a, b) => {
      let fieldA = a[sortCriteriaThird.field];
      let fieldB = b[sortCriteriaThird.field];

      if (sortCriteriaThird.field === 'animeEnglish') {
        fieldA = fieldA ? fieldA.toLowerCase() : '';
        fieldB = fieldB ? fieldB.toLowerCase() : '';
      } else if (sortCriteriaThird.field === 'dateStart') {
        fieldA = new Date(fieldA);
        fieldB = new Date(fieldB);
      } else if (sortCriteriaThird.field === 'score') {
        fieldA = parseFloat(fieldA);
        fieldB = parseFloat(fieldB);
      }

      if (sortCriteriaThird.order === 'asc') {
        return fieldA < fieldB ? -1 : fieldA > fieldB ? 1 : 0;
      } else {
        return fieldA > fieldB ? -1 : fieldA < fieldB ? 1 : 0;
      }
    });
  }

  // Calculate total pages and the results for the current page
  totalPagesThird = Math.ceil(filteredAnimeList.length / resultsPerPageThird);
  const startIndexThird = (page - 1) * resultsPerPageThird;
  const endIndexThird = startIndexThird + resultsPerPageThird;
  const paginatedResultsThird = filteredAnimeList.slice(
    startIndexThird,
    endIndexThird
  ); // Get results for the current page

  // Clear previous content
  filmListWrap.innerHTML = '';

  // Generate HTML for each anime
  paginatedResultsThird.map(anime => {
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
function setFilterWrapThird(letter) {
  filterLetterThird = letter;
  currentPageThird = 1; // Reset to the first page
  displayMatchesThird(searchDataListerThird, currentPageThird); // Update the results based on the new filter
}

// Function to change the filter category dynamically
function setFilter(category, value) {
  if (category === 'genres') {
    if (!filterCategoryThird.genres.includes(value)) {
      filterCategoryThird.genres.push(value); // Add genre if not already present
    } else {
      filterCategoryThird.genres = filterCategoryThird.genres.filter(
        genre => genre !== value
      ); // Remove genre if already present
    }
  } else {
    filterCategoryThird[category] = value; // Set other filters
  }
  currentPageThird = 1; // Reset to the first page
  displayMatchesThird(searchDataListerThird, currentPageThird); // Update the results based on the new filter
}

// Function to set sorting criteria
function setSortThird(field, order = 'asc') {
  sortCriteriaThird.field = field;
  sortCriteriaThird.order = order;
  currentPageThird = 1; // Reset to the first page
  displayMatchesThird(searchDataListerThird, currentPageThird); // Update the results based on the new sorting
}
