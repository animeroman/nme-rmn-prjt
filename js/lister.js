// Fetch the JSON data and call displayMatches directly
const jsonDataUrl = 'https://animeroman.github.io/Source/json/export.json';

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
    console.log(data); // Check if data is loaded correctly
    displayMatches(data); // Call displayMatches function with the parsed JSON
  })
  .catch(error => {
    console.error('Error fetching the anime data:', error);
  });

function displayMatches(animeList) {
  console.log('Displaying matches...'); // Debugging log to ensure function is called

  // Find the element with the class 'film_list-wrap'
  const filmListWrap = document.querySelector('.film_list-wrap');
  if (!filmListWrap) {
    console.error("No element with class 'film_list-wrap' found.");
    return;
  }

  // Clear the previous content in case this is run multiple times
  filmListWrap.innerHTML = '';

  // Function to generate the anime item HTML
  animeList.map(anime => {
    let animeEnglishName = anime.animeEnglish || 'Unknown Title';
    let animeOriginalName = anime.animeOriginal || 'Unknown Title';
    let animeDuration = anime.duration || 'Unknown Duration';
    let animeType = anime.type || 'Unknown Type';
    let posterLink = anime.poster || 'default-poster.png'; // Default image if no poster
    let pageLink = anime.page || '#';
    let subCount = anime.subCount || 0; // Handle missing subtitle count
    let episodes = anime.episodes || [];

    // Append HTML for each anime
    filmListWrap.innerHTML += `
            <div class="flw-item">
                <div class="film-poster">
                    <div class="tick ltr">
                        <div class="tick-item tick-sub">
                            <i class="fas fa-closed-captioning mr-1"></i>${subCount}
                        </div>
                    </div>
                    <img data-src="${posterLink}" class="film-poster-img lazyload" alt="${animeEnglishName}" />
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
