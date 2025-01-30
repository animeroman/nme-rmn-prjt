import { jsonData } from './config.js';

const resultsPerPage = 48; // Number of results per page
let currentPage = 1; // Keep track of the current page
let totalPages = 0; // Total pages based on the number of results
let filterLetter = ''; // Default filter by letter
let filterCategory = { genres: [], subDub: 'all' }; // Default filter, including genres and subDub
let sortCriteria = { field: '', order: 'asc' }; // Default sorting by field and order
const loadingPanel = document.querySelector('.loading-relative');

// Wait for the dataReady event to ensure jsonData is populated
document.addEventListener('dataReady', () => {
  displayMatches(jsonData, currentPage); // Display results for the first page
  loadingPanel.style.display = 'none';
});

// Function to count episodes with valid sub or dub links
export const countEpisodes = function (data, type = 'all') {
  try {
    let count = 0; // Initialize count to 0

    data.episodes.forEach(episode => {
      if (type === 'sub' || type === 'all') {
        // Check sub servers
        if (episode.subServer1 !== '#' || episode.subServer2 !== '#') {
          count++;
        }
      }
      if (type === 'dub' || type === 'all') {
        // Check dub servers
        if (episode.dubServer1 !== '#' || episode.dubServer2 !== '#') {
          count++;
        }
      }
    });

    return count; // Return the final count
  } catch (error) {
    throw error;
  }
};

// Display matches for the current page with the filter applied
function displayMatches(animeList, page) {
  try {
    const filmListWrap = document.querySelector('.film_list-wrap');
    if (!filmListWrap) {
      console.error("No element with class 'film_list-wrap' found.");
      return;
    }

    // Filter the animeList based on the filterLetter, filterCategory, and subDub
    let filteredAnimeList = animeList.filter(anime => {
      const animeFirstChar = anime.animeEnglish
        ? anime.animeEnglish.charAt(0).toLowerCase()
        : '';

      // Letter filter
      let letterMatch = true;
      if (filterLetter === '0-9') {
        letterMatch = /\d/.test(animeFirstChar); // Check if the first character is a number
      } else if (filterLetter === '#') {
        letterMatch = /[^a-z0-9]/i.test(animeFirstChar); // Check if the first character is a special character
      } else if (filterLetter !== 'all') {
        letterMatch = animeFirstChar === filterLetter.toLowerCase(); // Normal letter filter
      }

      // Category filter (based on filterCategory object)
      let categoryMatch = Object.keys(filterCategory).every(key => {
        if (key === 'genres') {
          // If genre filter is active, check if any genre matches
          if (filterCategory.genres.length === 0) return true; // No genre filter applied
          return (
            anime.genres &&
            filterCategory.genres.some(genre => anime.genres.includes(genre))
          );
        } else if (key === 'subDub') {
          // Check sub/dub filter
          if (filterCategory[key] === 'all') return true;
          if (filterCategory[key] === 'sub')
            return countEpisodes(anime, 'sub') > 0;
          if (filterCategory[key] === 'dub')
            return countEpisodes(anime, 'dub') > 0;
          return false;
        } else {
          // Normal category filters
          if (!filterCategory[key]) return true; // Ignore empty filters
          return anime[key] && anime[key] === filterCategory[key];
        }
      });

      return letterMatch && categoryMatch;
    });

    // Apply sorting before pagination
    if (sortCriteria.field) {
      filteredAnimeList.sort((a, b) => {
        let fieldA = a[sortCriteria.field];
        let fieldB = b[sortCriteria.field];

        if (sortCriteria.field === 'animeEnglish') {
          fieldA = fieldA ? fieldA.toLowerCase() : '';
          fieldB = fieldB ? fieldB.toLowerCase() : '';
        } else if (sortCriteria.field === 'dateStart') {
          fieldA = new Date(fieldA);
          fieldB = new Date(fieldB);
        } else if (sortCriteria.field === 'score') {
          fieldA = parseFloat(fieldA);
          fieldB = parseFloat(fieldB);
        }

        if (sortCriteria.order === 'asc') {
          return fieldA < fieldB ? -1 : fieldA > fieldB ? 1 : 0;
        } else {
          return fieldA > fieldB ? -1 : fieldA < fieldB ? 1 : 0;
        }
      });
    }

    // Calculate total pages and the results for the current page
    totalPages = Math.ceil(filteredAnimeList.length / resultsPerPage);
    const startIndex = (page - 1) * resultsPerPage;
    const endIndex = startIndex + resultsPerPage;
    const paginatedResults = filteredAnimeList.slice(startIndex, endIndex); // Get results for the current page

    // Generate HTML for each anime
    paginatedResults.map(anime => {
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
              <i class="fas fa-microphone mr-1"></i>${dubCount}
            </div>
            <div class="item item-flex item-sub">
              <i class="fas fa-closed-captioning mr-1"></i>${subCount}
            </div>
          </div>
          <div class="stick-mask bottom-right">
            <div class="tick-item tick-eps">EP: ${eposideCount}</div>
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
    `
      );
    });

    updatePagination(page); // Call updatePagination to manage the pagination controls
  } catch (error) {
    throw error;
  }
}

// Update pagination controls
function updatePagination(currentPage) {
  try {
    const paginationPlace = document.querySelector('.pagination-pages');
    if (!paginationPlace) {
      console.error("No element with class 'pagination-pages' found.");
      return;
    }

    let paginationHTML = '';

    // Calculate start and end page numbers
    let startPage = Math.max(currentPage - 1, 1);
    let endPage = Math.min(currentPage + 1, totalPages);

    // Ensure exactly 3 pages are displayed (if possible)
    if (endPage - startPage < 2) {
      if (startPage === 1) {
        endPage = Math.min(3, totalPages);
      } else if (endPage === totalPages) {
        startPage = Math.max(totalPages - 2, 1);
      }
    }

    // First page button
    if (currentPage > 1) {
      paginationHTML += `
      <li class="page-item">
        <a title="First" class="page-link" href="#" onclick="goToPage(1)">&laquo;</a>
      </li>`;
    }

    // Previous page button
    if (currentPage > 1) {
      paginationHTML += `
      <li class="page-item">
        <a title="Previous" class="page-link" href="#" onclick="goToPage(${
          currentPage - 1
        })">&lsaquo;</a>
      </li>`;
    }

    // Page numbers
    for (let i = startPage; i <= endPage; i++) {
      if (i === currentPage) {
        paginationHTML += `
        <li class="page-item active"><a class="page-link">${i}</a></li>`;
      } else {
        paginationHTML += `
        <li class="page-item"><a class="page-link" href="#" onclick="goToPage(${i})">${i}</a></li>`;
      }
    }

    // Next page button
    if (currentPage < totalPages) {
      paginationHTML += `
      <li class="page-item">
        <a title="Next" class="page-link" href="#" onclick="goToPage(${
          currentPage + 1
        })">&rsaquo;</a>
      </li>`;
    }

    // Last page button
    if (currentPage < totalPages) {
      paginationHTML += `
      <li class="page-item">
        <a title="Last" class="page-link" href="#" onclick="goToPage(${totalPages})">&raquo;</a>
      </li>`;
    }

    paginationPlace.innerHTML = paginationHTML; // Update the pagination controls
  } catch (error) {
    throw error;
  }
}

// Go to the specified page
function goToPage(page) {
  try {
    currentPage = page;
    displayMatches(jsonData, page); // Redisplay matches for the new page
  } catch (error) {
    throw error;
  }
}

// Function to change the filter letter dynamically
function setFilterLetter(letter) {
  try {
    filterLetter = letter;
    currentPage = 1; // Reset to the first page
    displayMatches(jsonData, currentPage); // Update the results based on the new filter
  } catch (error) {
    throw error;
  }
}

// Function to change the filter category dynamically
function setFilter(category, value) {
  try {
    if (category === 'genres') {
      if (!filterCategory.genres.includes(value)) {
        filterCategory.genres.push(value); // Add genre if not already present
      } else {
        filterCategory.genres = filterCategory.genres.filter(
          genre => genre !== value
        ); // Remove genre if already present
      }
    } else {
      filterCategory[category] = value; // Set other filters, including subDub
    }
    currentPage = 1; // Reset to the first page
    displayMatches(jsonData, currentPage); // Update the results based on the new filter
  } catch (error) {
    throw error;
  }
}

// Function to set sorting criteria
function setSort(field, order = 'asc') {
  try {
    sortCriteria.field = field;
    sortCriteria.order = order;
    currentPage = 1; // Reset to the first page
    displayMatches(jsonData, currentPage); // Update the results based on the new sorting
  } catch (error) {
    throw error;
  }
}

// Attach to the global window object
window.setFilterLetter = setFilterLetter;
window.setFilter = setFilter;
window.setSort = setSort;
window.goToPage = goToPage;
