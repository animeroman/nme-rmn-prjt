'use strict';

document
  .querySelector('#filter-form')
  .addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get the search keyword from the input or URL
    let keyword = document.querySelector('input[name="keyword"]').value.trim();

    // Get existing parameters from the URL (this preserves the current ones)
    let params = new URLSearchParams(window.location.search);

    // If keyword is found in the URL but not in the input (e.g., refreshed page), retain it
    if (!keyword) {
      keyword = params.get('keyword') || '';
    }

    // Update the 'keyword' parameter, or delete it if empty
    if (keyword) {
      params.set('keyword', keyword);
    } else {
      params.delete('keyword');
    }

    // Get filter values from the form
    const typeFilter = document.querySelector('select[name="type"]').value;
    const statusFilter = document.querySelector('select[name="status"]').value;
    const ratedFilter = document.querySelector('select[name="rated"]').value;
    const genreFilter = document.querySelector('input#f-genre-ids').value;
    const seasonFilter = document.querySelector('select[name="season"]').value;
    const languageFilter = document.querySelector('select[name="language"]')
      .value;
    const scoreFilter = document.querySelector('select[name="score"]').value;
    const sortFilter = document.querySelector('select[name="sort"]').value;

    // Update or remove URL parameters based on filter values
    typeFilter ? params.set('type', typeFilter) : params.delete('type');
    statusFilter ? params.set('status', statusFilter) : params.delete('status');
    ratedFilter ? params.set('rated', ratedFilter) : params.delete('rated');
    genreFilter ? params.set('genres', genreFilter) : params.delete('genres');
    seasonFilter ? params.set('season', seasonFilter) : params.delete('season');
    languageFilter
      ? params.set('language', languageFilter)
      : params.delete('language');
    scoreFilter ? params.set('score', scoreFilter) : params.delete('score');
    sortFilter ? params.set('sort', sortFilter) : params.delete('sort');

    // Update the URL without reloading the page
    window.history.replaceState(
      {},
      '',
      `${window.location.pathname}?${params.toString()}`
    );

    // Re-run the search and apply filters
    displayMatches(keyword, 1); // Reset to the first page
  });

// Function to set selected values in the filters based on URL parameters
function setFilterValuesFromURL() {
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
}

// Call the function to set the filter values on page load
window.addEventListener('load', setFilterValuesFromURL);

function displayMatches(inputValue, page) {
  const matchArray = findMatches(inputValue, searchDataEngine); // Get matches

  // Get filters from URL
  const typeFilter = getQueryParam('type');
  const statusFilter = getQueryParam('status');
  const ratedFilter = getQueryParam('rated');
  const genreFilter = getQueryParam('genres');
  const seasonFilter = getQueryParam('season');
  const languageFilter = getQueryParam('language');
  const scoreFilter = getQueryParam('score');
  const sortFilter = getQueryParam('sort');

  // Filter results
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

    // Check for 'genres' filter
    const genreMatch =
      !genreFilter || (anime.genres && anime.genres.includes(genreFilter));

    // Return true if all filters match
    return (
      typeMatch &&
      statusMatch &&
      ratedMatch &&
      seasonMatch &&
      languageMatch &&
      scoreMatch &&
      genreMatch
    );
  });

  // Sort results
  if (sortFilter) {
    filteredArray.sort((a, b) => applySorting(sortFilter, a, b));
  }

  // Pagination logic
  totalPages = Math.ceil(filteredArray.length / resultsPerPage);
  const startIndex = (page - 1) * resultsPerPage;
  const endIndex = startIndex + resultsPerPage;
  const paginatedResults = filteredArray.slice(startIndex, endIndex);

  // Render results
  const html = paginatedResults
    .map(anime => {
      return `
            <div class="flw-item flw-item-big">
                <div class="film-poster">
                    <img data-src="${anime.poster}" class="film-poster-img lazyload" src="${anime.poster}" />
                    <a href="watch/${anime.page}.html" class="film-poster-ahref"><i class="fas fa-play"></i></a>
                </div>
                <div class="film-detail">
                    <h3 class="film-name">
                        <a href="watch/${anime.page}.html">${anime.animeEnglish}</a>
                    </h3>
                    <div class="fd-infor">
                        <span>${anime.type}</span>
                        <span class="dot"></span>
                        <span>${anime.duration}</span>
                    </div>
                </div>
            </div>`;
    })
    .join('');

  document.querySelector('.film_list-wrap').innerHTML = html;
  updatePagination(page); // Update pagination controls
}

function getQueryParam(param) {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get(param);
}

function mapType(typeValue) {
  const typeMap = {
    '1': 'Movie',
    '2': 'TV',
    '3': 'OVA',
    '4': 'ONA',
    '5': 'Special',
    '6': 'Music'
  };
  return typeMap[typeValue] || '';
}

function mapStatus(statusValue) {
  const statusMap = {
    '1': 'Finished Airing',
    '2': 'Currently Airing',
    '3': 'Not yet aired'
  };
  return statusMap[statusValue] || '';
}

function mapRated(ratedValue) {
  const ratedMap = {
    '1': 'G',
    '2': 'PG',
    '3': 'PG-13',
    '4': 'R',
    '5': 'R+',
    '6': 'Rx'
  };
  return ratedMap[ratedValue] || '';
}

function mapSeason(seasonValue) {
  const seasonMap = {
    '1': 'Spring',
    '2': 'Summer',
    '3': 'Fall',
    '4': 'Winter'
  };
  return seasonMap[seasonValue] || '';
}

function mapLanguage(languageValue) {
  const languageMap = { '1': 'SUB', '2': 'DUB', '3': 'SUB & DUB' };
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
