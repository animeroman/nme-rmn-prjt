'use strict';
import { endpoint } from './config.js';

// Function to fetch and display recommendations
function fetchAndDisplayRecommendations(currentPage) {
  // Fetch data from the JSON endpoint
  fetch(endpoint)
    .then(response => response.json())
    .then(data => {
      // Find the current anime data
      const currentAnime = data.find(anime => anime.page === currentPage);

      if (!currentAnime) {
        console.warn('No matching anime found for recommendations.');
        return;
      }

      console.log('Current Anime:', currentAnime);

      // Find similar anime based on genres and score
      const similarAnime = findSimilarAnime(currentAnime, data);

      console.log('Similar Anime:', similarAnime);

      // Update the "Recommended for you" section
      updateRecommendationsSection(similarAnime);
    })
    .catch(error => {
      console.error('Error fetching recommendations:', error);
    });
}

// Function to find similar anime based on genres and score
function findSimilarAnime(currentAnime, allAnime) {
  return allAnime
    .filter(anime => anime.page !== currentAnime.page) // Exclude the current anime
    .map(anime => {
      // Calculate matching genres and unrelated categories
      const matchingGenres = anime.genres.filter(genre =>
        currentAnime.genres.includes(genre)
      );
      const unrelatedGenres = anime.genres.filter(
        genre => !currentAnime.genres.includes(genre)
      );

      return {
        ...anime,
        matchingGenresCount: matchingGenres.length,
        unrelatedGenresCount: unrelatedGenres.length,
        score: parseFloat(anime.score) || 0, // Ensure score is a number
      };
    })
    .sort((a, b) => {
      // Sort by the number of matching genres (descending)
      if (b.matchingGenresCount !== a.matchingGenresCount) {
        return b.matchingGenresCount - a.matchingGenresCount;
      }

      // Then sort by the number of unrelated genres (ascending)
      if (a.unrelatedGenresCount !== b.unrelatedGenresCount) {
        return a.unrelatedGenresCount - b.unrelatedGenresCount;
      }

      // Finally, sort by score (descending) as a tie-breaker
      return b.score - a.score;
    })
    .slice(0, 18); // Limit to 18 recommendations
}

// Function to update the recommendations section in the HTML
function updateRecommendationsSection(similarAnime) {
  const recommendationsContainer = document.querySelector('.recommned-wrapper');

  if (!recommendationsContainer) {
    console.error('Recommendations container not found!');
    return;
  }

  // Clear previous content
  recommendationsContainer.innerHTML = '';

  // Populate with similar anime
  similarAnime.forEach((anime, index) => {
    const isHighlighted = index === 0; // Highlight the first anime in the sorted list
    const recommendationHTML = `
      <div class="flw-item ${isHighlighted ? 'highlight' : ''}">
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
            <span class="dot"></span>
            <span class="fdi-item fdi-score">${anime.score.toFixed(2)}</span>
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
