'use strict';
// JSON data point
const endpoint_Watch =
  'https://animeroman.github.io/nme-rmn-prjt/json/export2.json';

// Store the selected server type globally to remember it across episodes
let selectedServerType = localStorage.getItem('selectedServerType') || 'sub'; // Default to 'sub'
let selectedServerIndex = localStorage.getItem('selectedServerIndex') || 1; // Default to 'SUB-1' or 'DUB-1'
let selectedEpisode = localStorage.getItem('selectedEpisode') || 1; // Default to Episode 1
let selectedDropdownPage = localStorage.getItem('selectedDropdownPage') || 1; // Default to the first dropdown page
let selectedDropdownCurrentPage =
  localStorage.getItem('selectedDropdownCurrentPage') || `EPS: 001-100`; // Default dropdown text

// Add this variable before the loop to track the count of episodes
let totalEpisodes = 0;

// Function to update the breadcrumb with the anime type, href, and text
function updateAniscDetail(animeData) {
  // Define mapping between types and href links
  const typeToHrefMap = {
    Movie: '../movie.html',
    TV: '../tv.html',
    OVA: '../ova.html',
    ONA: '../ona.html',
    Special: '../special.html',
    Music: '../music.html',
  };

  const seasonToHrefMap = {
    Spring: '../season/spring.html',
    Summer: '../season/summer.html',
    Fall: '../season/fall.html',
    Winter: '../season/winter.html',
  };

  // Select the breadcrumb element
  const breadcrumb = document.querySelector('ol.breadcrumb');
  if (!breadcrumb) {
    console.error('Breadcrumb element not found!');
    return;
  }

  // Update the first breadcrumb item's href and text with the season
  const fisrtBreadcrumbItem = breadcrumb.querySelectorAll('li')[0];
  if (fisrtBreadcrumbItem) {
    const link = fisrtBreadcrumbItem.querySelector('a');
    if (link) {
      link.textContent = animeData.season; // Replace text with "season"
      if (seasonToHrefMap[animeData.season]) {
        link.setAttribute('href', seasonToHrefMap[animeData.season]); // Update href
      } else {
        console.warn(`No href mapping found for season: ${animeData.season}`);
      }
    }
  } else {
    console.error('First breadcrumb item not found!');
  }

  // Update the second breadcrumb item's href and text with the type
  const secondBreadcrumbItem = breadcrumb.querySelectorAll('li')[1];
  if (secondBreadcrumbItem) {
    const link = secondBreadcrumbItem.querySelector('a');
    if (link) {
      link.textContent = animeData.type; // Replace text with "type"
      if (typeToHrefMap[animeData.type]) {
        link.setAttribute('href', typeToHrefMap[animeData.type]); // Update href
      } else {
        console.warn(`No href mapping found for type: ${animeData.type}`);
      }
    }
  } else {
    console.error('Second breadcrumb item not found!');
  }

  // Update the third breadcrumb item's text and 'data-jname'
  const thirdBreadcrumbItem = breadcrumb.querySelectorAll('li')[2];
  if (thirdBreadcrumbItem) {
    thirdBreadcrumbItem.textContent = animeData.animeEnglish; // Replace text with "animeEnglish"
    thirdBreadcrumbItem.setAttribute('data-jname', animeData.animeOriginal); // Replace data-jname with "animeOriginal"
  } else {
    console.error('Third breadcrumb item not found!');
  }

  // Update the film-name and anisc-detail content
  const filmNameElement = document.querySelector('h2.film-name');
  if (filmNameElement) {
    filmNameElement.textContent = animeData.animeEnglish; // Update film-name
  } else {
    console.error('film-name element not found!');
  }

  const aniscDetailElement = document.querySelector('h2.film-name');
  if (aniscDetailElement) {
    aniscDetailElement.setAttribute('data-jname', animeData.animeOriginal); // Update data-jname
  } else {
    console.error('anisc-detail element not found!');
  }

  // Update the tick-pg
  const TickItemPg = document.querySelector('.tick-pg');
  if (TickItemPg) {
    TickItemPg.textContent = animeData.rated; // Update tick-pg
  } else {
    console.error('div.tick-pg element not found!');
  }

  // Update the tick-sub
  const TickItemSub = document.querySelector('.tick-sub');
  if (TickItemSub) {
    TickItemSub.textContent = animeData.eposideCount; // Update tick-sub
  } else {
    console.error('div.tick-sub element not found!');
  }

  // Update the tick-dub
  const TickItemDub = document.querySelector('.tick-dub');
  if (TickItemDub) {
    TickItemDub.textContent = animeData.eposideCount; // Update tick-dub
  } else {
    console.error('div.tick-dub element not found!');
  }

  // Update the tick-eps
  const TickItemEps = document.querySelector('.tick-eps');
  if (TickItemEps) {
    TickItemEps.textContent = animeData.eposideCount; // Update tick-eps
  } else {
    console.error('div.tick-eps element not found!');
  }

  // Update the item-type
  const ItemType = document.querySelector('.item-type');
  if (ItemType) {
    ItemType.textContent = animeData.type; // Update item-type
  } else {
    console.error('span.item-type element not found!');
  }

  // Update the item-duration
  const ItemDuration = document.querySelector('.item-duration');
  if (ItemDuration) {
    ItemDuration.textContent = animeData.duration; // Update item-duration
  } else {
    console.error('span.item-duration element not found!');
  }

  // Update the film-buttons' href
  const filmButtons = document.querySelector('.film-buttons a'); // Target the <a> tag inside .film-buttons
  if (filmButtons) {
    if (animeData && animeData.page) {
      // Ensure animeData.page exists
      filmButtons.setAttribute('href', `../watch/${animeData.page}.html`); // Update the href
    } else {
      console.error('animeData.page is missing or invalid!');
    }
  } else {
    console.error('.film-buttons <a> element not found!');
  }
}

// Function to update the poster image source and alt attributes
function updatePosterImage(animeData) {
  // Select the img element with class 'film-poster-img'
  const posterImage = document.querySelector('img.film-poster-img');
  if (!posterImage) {
    console.error('Poster image element not found!');
    return;
  }

  // Update the src attribute with the poster URL from the animeData
  posterImage.setAttribute('src', animeData.poster);

  // Update the alt attribute with the animeEnglish from the animeData
  posterImage.setAttribute('alt', animeData.animeEnglish);
}

// Function to update anime information in the anisc-info section
function updateAnimeInfo(animeData) {
  const aniscInfo = document.querySelector('.anisc-info');
  if (!aniscInfo) {
    console.error('anisc-info container not found!');
    return;
  }

  const items = aniscInfo.querySelectorAll('.item');

  if (items[0]) {
    const textDiv = items[0].querySelector('.text');
    if (textDiv) textDiv.textContent = animeData.description;

    // Update the film-description div with the description
    const filmDescriptionDiv = document
      .querySelector('.film-description')
      .querySelector('.text');
    if (filmDescriptionDiv)
      filmDescriptionDiv.textContent = animeData.description;
  }

  if (items[1]) {
    const nameSpan = items[1].querySelector('.name');
    if (nameSpan) nameSpan.textContent = animeData.japanese;
  }

  if (items[2]) {
    const nameSpan = items[2].querySelector('.name');
    if (nameSpan) nameSpan.textContent = animeData.synonyms[0];
  }

  if (items[3]) {
    const nameSpan = items[3].querySelector('.name');
    if (nameSpan)
      nameSpan.textContent = `${animeData.dateStart} to ${animeData.dateEnd}`;
  }

  if (items[4]) {
    const nameSpan = items[4].querySelector('.name');
    if (nameSpan) nameSpan.textContent = animeData.season;
  }

  if (items[5]) {
    const nameSpan = items[5].querySelector('.name');
    if (nameSpan) nameSpan.textContent = animeData.duration;
  }

  if (items[6]) {
    const nameSpan = items[6].querySelector('.name');
    if (nameSpan) nameSpan.textContent = animeData.status;
  }

  if (items[7]) {
    const scoreSpan = items[7].querySelector('span');
    if (scoreSpan) scoreSpan.textContent = animeData.score;
  }

  if (items[8]) {
    // Populate genres for the ninth item
    const genreContainer = items[8];
    genreContainer.innerHTML = `<span class="item-head">Genres:</span>`; // Clear existing content and add header

    // Add each genre as a link
    animeData.genres.forEach(genre => {
      const genreLink = document.createElement('a');
      genreLink.href = `genre/${genre.toLowerCase().replace(/\s+/g, '-')}.html`;
      genreLink.title = genre;
      genreLink.textContent = genre;
      genreContainer.appendChild(genreLink);
    });
  }

  if (items[9]) {
    // Populate studios for the tenth item
    const studiosContainer = items[9];
    studiosContainer.innerHTML = `<span class="item-head">Studios:</span>`; // Clear existing content and add header

    // Add each studio as a link
    animeData.studios.forEach(studio => {
      const studioLink = document.createElement('a');
      studioLink.classList.add('name');
      studioLink.href = `producer/${studio
        .toLowerCase()
        .replace(/\s+/g, '-')}.html`;
      studioLink.textContent = studio;

      // Add a comma if it's not the last studio
      studiosContainer.appendChild(studioLink);
      if (studio !== animeData.studios[animeData.studios.length - 1]) {
        studiosContainer.appendChild(document.createTextNode(', '));
      }
    });
  }

  if (items[10]) {
    // Populate producers for the eleventh item
    const producersContainer = items[10];
    producersContainer.innerHTML = `<span class="item-head">Producers:</span>`; // Clear existing content and add header

    animeData.producers.forEach(producer => {
      const producerLink = document.createElement('a');
      producerLink.classList.add('name');
      producerLink.href = `producer/${producer
        .toLowerCase()
        .replace(/\s+/g, '-')}.html`;
      producerLink.textContent = producer;

      producersContainer.appendChild(producerLink);
      if (producer !== animeData.producers[animeData.producers.length - 1]) {
        producersContainer.appendChild(document.createTextNode(', '));
      }
    });
  }
}

// Function to generate connection HTML and add it to the page
function updateConnections(connections, allAnimeData) {
  const connectionWrapper = document.querySelector('.connection-wrapper');
  if (!connectionWrapper) {
    console.error('Connection wrapper element not found!');
    return;
  }

  // Clear existing connections
  connectionWrapper.innerHTML = '';

  // Match connection ids with anime data
  const matchedConnections = connections.map(conn =>
    allAnimeData.find(anime => anime.id === conn.id)
  );

  // Generate HTML for each matched connection
  matchedConnections.forEach(connection => {
    if (connection) {
      const connectionHTML = `
        <div class="flw-item flw-item-active">
          <div class="film-poster">
            <div class="tick tick-rate">18+</div>

              <div class="tick ltr">
                <div class="tick-item tick-sub">
                  <i class="fas fa-closed-captioning mr-1"></i>13
                </div>

                <div class="tick-item tick-dub">
                  <i class="fas fa-microphone mr-1"></i>13
                </div>

              <div class="tick-item tick-eps">13</div>
            </div>

            <img data-src="${connection.poster}" src="${connection.poster}" class="film-poster-img lazyloaded" alt="${connection.animeEnglish}">
            <a href="watch/${connection.page}" class="film-poster-ahref item-qtip" title="${connection.animeEnglish}">
              <i class="fas fa-play"></i>
            </a>
          </div>
          <div class="film-detail">
            <h3 class="film-name">
              <a href="page/${connection.page}" title="${connection.animeEnglish}" class="dynamic-name" data-jname="${connection.animeOriginal}">
                ${connection.animeEnglish}
              </a>
            </h3>
            <div class="fd-infor">
              <span class="fdi-item">${connection.type}</span>
              <span class="dot"></span>
              <span class="fdi-item fdi-duration">${connection.duration}</span>
              <span class="dot"></span>
              <span class="fdi-item fdi-score">${connection.score}</span>
            </div>
          </div>
          <div class="clearfix"></div>
        </div>`;
      connectionWrapper.insertAdjacentHTML('beforeend', connectionHTML);
    }
  });
}

// Fetch the anime data from the endpoint and run the episode list creation
window.onload = function () {
  // Step 1: Extract the "page" part from the URL (e.g., 'sgt-frog-516.html')
  const currentPage = window.location.pathname
    .split('/')
    .pop()
    .replace('.html', '');
  console.log(`Current page: ${currentPage}`); // Result: 'sgt-frog-516'

  // Step 2: Fetch data from the JSON endpoint
  const anime = [];
  fetch(endpoint_Watch)
    .then(blob => blob.json())
    .then(data => {
      anime.push(...data); // Push the fetched data into the 'anime' array

      // Step 3: Find the anime data that matches the current page after data is fetched
      const matchingAnime = findPathname(currentPage, anime);

      if (matchingAnime.length > 0) {
        console.log('Found matching anime:', matchingAnime[0]);

        // Step 4: Update the anisc-detail section with film name and breadcrumb data
        updateAniscDetail(matchingAnime[0]);

        // Step 5: Update the poster image source and alt attributes
        updatePosterImage(matchingAnime[0]);

        // Step 6: Update anime information in the anisc-info section
        updateAnimeInfo(matchingAnime[0]);

        // Step 7: Update connections
        if (
          matchingAnime[0].connections &&
          matchingAnime[0].connections.length > 0
        ) {
          updateConnections(matchingAnime[0].connections, anime);
        }
      } else {
        console.warn('No matching anime found for this page.');
      }
    })
    .catch(error => {
      console.error('Error fetching JSON:', error);
    });

  // window.onload for recommend.js: Fetch and display recommendations
  fetchAndDisplayRecommendations(currentPage);
};

// Utility function to find the current anime in the JSON data
function findPathname(currentPage, data) {
  return data.filter(anime => anime.page === currentPage);
}
