'use strict';

// JSON data endpoint for anime information
const endpoint_Recommend =
  'https://animeroman.github.io/nme-rmn-prjt/json/export2.json';

// Function to fetch and display recommendations
function fetchAndDisplayRecommendations(currentPage) {
  // Fetch data from the JSON endpoint
  fetch(endpoint_Recommend)
    .then(response => response.json())
    .then(data => {
      // Find the current anime data
      const currentAnime = data.find(anime => anime.page === currentPage);

      if (!currentAnime) {
        console.warn('No matching anime found for recommendations.');
        return;
      }

      console.log('Current Anime:', currentAnime);

      // Find similar anime based on genres
      const similarAnime = findSimilarAnime(currentAnime, data);

      console.log('Similar Anime:', similarAnime);

      // Update the "Recommended for you" section
      updateRecommendationsSection(similarAnime);
    })
    .catch(error => {
      console.error('Error fetching recommendations:', error);
    });
}

// Function to find similar anime based on genres
function findSimilarAnime(currentAnime, allAnime) {
  return allAnime
    .filter(anime => {
      // Exclude the current anime from recommendations
      if (anime.page === currentAnime.page) return false;

      // Check for shared genres
      return anime.genres.some(genre => currentAnime.genres.includes(genre));
    })
    .slice(0, 18); // Limit to 18 recommendations
}

// Function to update the recommendations section in the HTML
function updateRecommendationsSection(similarAnime) {
  const recommendationsContainer = document.querySelector('.film_list-wrap');

  if (!recommendationsContainer) {
    console.error('Recommendations container not found!');
    return;
  }

  // Clear previous content
  recommendationsContainer.innerHTML = '';

  // Populate with similar anime
  similarAnime.forEach(anime => {
    const recommendationHTML = `
      <div class="flw-item">
        <div class="film-poster">
          <div class="tick tick-rate">18+</div>
          <div class="tick ltr">
            <div class="tick-item tick-sub">
              <i class="fas fa-closed-captioning mr-1"></i>${anime.eposideCount}
            </div>
            <div class="tick-item tick-dub">
              <i class="fas fa-microphone mr-1"></i>${anime.eposideCount}
            </div>
            <div class="tick-item tick-eps">${anime.eposideCount}</div> 
          </div>
          <img
            data-src="${anime.poster}"
            src="${anime.poster}"
            class="film-poster-img lazyload"
            alt="${anime.animeEnglish}"
          />
          <a
            href="watch/${anime.page}.html"
            class="film-poster-ahref item-qtip"
            title="${anime.animeEnglish}"
          >
            <i class="fas fa-play"></i>
          </a>
        </div>
        <div class="film-detail">
          <h3 class="film-name">
            <a
              href="page/${anime.page}.html"
              title="${anime.animeEnglish}"
              class="dynamic-name"
              data-jname="${anime.animeOriginal}"
            >
              ${anime.animeEnglish}
            </a>
          </h3>
          <div class="fd-infor">
            <span class="fdi-item">${anime.type}</span>
            <span class="dot"></span>
            <span class="fdi-item fdi-duration">${anime.duration}</span>
          </div>
        </div>
        <div class="clearfix"></div>
      </div>
    `;
    recommendationsContainer.insertAdjacentHTML(
      'beforeend',
      recommendationHTML
    );
  });
}

// Script initialization (mimicking watch-page.js style)
window.onload = function () {
  // Step 1: Extract the "page" part from the URL (e.g., 'sgt-frog-516.html')
  const currentPage = window.location.pathname
    .split('/')
    .pop()
    .replace('.html', '');

  console.log(`Current page: ${currentPage}`); // Result: 'sgt-frog-516'

  // Step 2: Fetch and display recommendations
  fetchAndDisplayRecommendations(currentPage);
};
