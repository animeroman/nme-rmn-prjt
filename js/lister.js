const resultsPerPage = 36; // Number of results per page
let currentPage = 1; // Keep track of the current page
let totalPages = 0; // Total pages based on the number of results

const jsonDataUrl = 'https://animeroman.github.io/Source/json/main-search.json';
const searchDataEngine = [];

fetch(jsonDataUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return response.json(); // Parse the JSON
  })
  .then(data => {
    searchDataEngine.push(...data); // Store the data
    displayMatches(searchDataEngine, currentPage); // Display results for the first page
  })
  .catch(error => {
    console.error('Error fetching the anime data:', error);
  });

// Display matches for the current page
function displayMatches(animeList, page) {
  const filmListWrap = document.querySelector('.film_list-wrap');
  if (!filmListWrap) {
    console.error("No element with class 'film_list-wrap' found.");
    return;
  }

  // Calculate total pages and the results for the current page
  totalPages = Math.ceil(animeList.length / resultsPerPage);
  const startIndex = (page - 1) * resultsPerPage;
  const endIndex = startIndex + resultsPerPage;
  const paginatedResults = animeList.slice(startIndex, endIndex); // Get results for the current page

  // Clear previous content
  filmListWrap.innerHTML = '';

  // Generate HTML for each anime
  paginatedResults.map(anime => {
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

  updatePagination(page); // Call updatePagination to manage the pagination controls
}

// Update pagination controls
function updatePagination(currentPage) {
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
        <a title="Previous" class="page-link" href="#" onclick="goToPage(${currentPage -
          1})">&lsaquo;</a>
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
        <a title="Next" class="page-link" href="#" onclick="goToPage(${currentPage +
          1})">&rsaquo;</a>
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
}

// Go to the specified page
function goToPage(page) {
  currentPage = page;
  displayMatches(searchDataEngine, page); // Redisplay matches for the new page
}
