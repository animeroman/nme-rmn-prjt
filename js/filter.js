'use strict';

document
  .querySelector('#filter-form')
  .addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Get the search keyword
    let keyword =
      getQueryParam('keyword') ||
      document.querySelector('input[name="keyword"]').value.trim();

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

    // Update URL parameters
    let params = new URLSearchParams(window.location.search);

    keyword ? params.set('keyword', keyword) : params.delete('keyword');
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

    // Update the URL without reloading
    window.history.pushState({}, '', `${window.location.pathname}?${params}`);

    // Re-run the search and apply filters
    displayMatches(keyword, 1); // Reset to the first page
  });

function displayMatches(inputValue, page) {
  const matchArray = findMatches(inputValue, searchData); // Get matches

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
