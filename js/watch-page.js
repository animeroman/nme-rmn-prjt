'use strict';
import { jsonData } from './config.js';
import { fetchAndDisplayRecommendations } from './recommend.js';

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

  // Update the film-description
  const filmDescription = document.querySelector('.film-description .text');
  if (filmDescription) {
    filmDescription.textContent = animeData.description; // Update film-description
  } else {
    console.error('.film-description element not found!');
  }

  // Update the film-description
  const blockView = document.querySelector('.block a');
  if (blockView) {
    blockView.setAttribute('href', `../page/${animeData.page}.html`); // Update block a
  } else {
    console.error('.block a element not found!');
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

// Function to create the episode list
function createEpisodeList(data) {
  const detailInforContent = document.querySelector('.detail-infor-content');
  const seasonBlockContent = document.querySelector('.seasons-block');
  const eposideLabelContent = document.querySelector('.ssc-label');

  // Use a loop to find the total number of episodes or the highest episode number
  data.episodes.forEach(episode => {
    // Update totalEpisodes with the highest episode number
    totalEpisodes = Math.max(totalEpisodes, episode.episodeNumber);
  });

  // Function to create the dropdown for episodes
  function createEpisodeDropdown(totalEpisodes) {
    if (totalEpisodes > 100) {
      seasonBlockContent.classList.add('seasons-block-max');

      let html = `
        <div
            class="ssc-name"
            data-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
        >
            <i class="fas fa-list mr-3"></i>
            <span id="current-page">${selectedDropdownCurrentPage}</span>
            <i class="fas fa-angle-down ml-2"></i>
        </div>
        <div class="dropdown-menu dropdown-menu-model" aria-labelledby="ssc-list">
        `;

      // Generate dropdown items for every 100 episodes
      for (let i = 0; i < Math.ceil(totalEpisodes / 100); i++) {
        const start = i * 100 + 1;
        const end = Math.min((i + 1) * 100, totalEpisodes);
        const isActive = i + 1 == selectedDropdownPage ? 'active' : ''; // Highlight last selected page
        const checkIcon = i + 1 == selectedDropdownPage ? 'inline' : 'none'; // Show check icon for last selected
        html += `
            <a
                data-page="${i + 1}"
                href="javascript:;"
                class="dropdown-item ep-page-item ${isActive}"
            >
                EPS: ${String(start).padStart(3, '0')}-${String(end).padStart(
                  3,
                  '0'
                )}<i
                style="display: ${checkIcon};"
                class="fas fa-check ic-active ml-2"
                ></i>
            </a>
            `;
      }

      html += `</div>`;
      eposideLabelContent.insertAdjacentHTML('beforeend', html);
    }
  }

  // Function to display episodes for the selected section
  function displayEpisodesForSection(episodes, start, end) {
    const container = document.querySelector('.ss-list');
    if (!container) {
      console.error('Episode container not found!');
      return;
    }

    container.innerHTML = ''; // Clear previous episodes

    // Filter episodes within the selected range and add them to the container
    const filteredEpisodes = episodes.filter(
      ep => ep.episodeNumber >= start && ep.episodeNumber <= end
    );

    if (filteredEpisodes.length === 0) {
      container.innerHTML = '<p>No episodes available for this section.</p>';
      return;
    }

    filteredEpisodes.forEach(episode => {
      const isActive = episode.episodeNumber == selectedEpisode ? 'active' : ''; // Highlight active episode
      const episodeHTML = `
        <a
            title="Episode ${episode.episodeNumber}"
            class="ssl-item ep-item"
            data-number="${episode.episodeNumber}"
            data-subserver1="${episode.subServer1}"
            data-subserver2="${episode.subServer2}"
            data-dubserver1="${episode.dubServer1}"
            data-dubserver2="${episode.dubServer2}"
            href="javascript:;"
        >
            <div class="ssli-order">${episode.episodeNumber}</div>
            <div class="ssli-detail">
                <div class="ep-name e-dynamic-name" title="${episode.title}">
                    ${episode.title}
                </div>
            </div>
            <div class="ssli-btn">
                <div class="btn btn-circle">
                    <i class="fas fa-play"></i>
                </div>
            </div>
            <div class="clearfix"></div>
        </a>
        `;
      container.insertAdjacentHTML('beforeend', episodeHTML);
    });

    // Add click event listener to each episode link
    const episodeLinks = container.querySelectorAll('.ep-item');
    episodeLinks.forEach(link => {
      link.addEventListener('click', function () {
        // Get server URLs from the clicked element's data attributes
        const subServer1 = this.getAttribute('data-subserver1');
        const subServer2 = this.getAttribute('data-subserver2');
        const dubServer1 = this.getAttribute('data-dubserver1');
        const dubServer2 = this.getAttribute('data-dubserver2');
        const episodeNumber = this.getAttribute('data-number');

        // Store the selected episode in localStorage
        localStorage.setItem('selectedEpisode', episodeNumber);

        // Update the window location
        history.pushState(null, '', `?episode=${episodeNumber}`);

        // Remove 'active' class from previously selected episode
        container.querySelectorAll('.ep-item').forEach(ep => {
          ep.classList.remove('active');
        });

        // Add 'active' class to the clicked episode
        this.classList.add('active');

        // Update the server list based on the selected episode
        updateServerList(subServer1, subServer2, dubServer1, dubServer2);
      });
    });

    // Auto-click the previously selected episode or the first one by default
    const selectedEpisodeElement = container.querySelector(
      `.ep-item[data-number="${selectedEpisode}"]`
    );
    if (selectedEpisodeElement) {
      selectedEpisodeElement.click();
    } else {
      // If no episode is selected (e.g., first page load), select the first episode
      const firstEpisodeElement = container.querySelector('.ep-item');
      if (firstEpisodeElement) {
        firstEpisodeElement.click();
      }
    }
  }

  // Function to attach click event listeners to dropdown items
  function attachDropdownListeners(totalEpisodes, episodes) {
    const dropdownItems = document.querySelectorAll('.ep-page-item');

    dropdownItems.forEach((item, index) => {
      item.addEventListener('click', function () {
        // Update the displayed text to match the clicked dropdown item
        const currentPageText = this.textContent.trim();
        document.getElementById('current-page').textContent = currentPageText;

        // Store the selected dropdown page text in localStorage
        localStorage.setItem('selectedDropdownCurrentPage', currentPageText);

        // Remove active state from all items and add to clicked one
        dropdownItems.forEach(el => {
          el.querySelector('i').style.display = 'none';
          el.classList.remove('active');
        });
        this.querySelector('i').style.display = 'inline';
        this.classList.add('active');

        // Store the selected dropdown page in localStorage
        const selectedPage = this.getAttribute('data-page');
        localStorage.setItem('selectedDropdownPage', selectedPage);

        // Get the start and end episode range for the clicked section
        const start = index * 100 + 1;
        const end = Math.min((index + 1) * 100, totalEpisodes);

        // Display episodes for the selected section
        displayEpisodesForSection(episodes, start, end);
      });
    });
  }

  // Function to add the episode list container
  function addEpisodeListContainer() {
    const ssList =
      totalEpisodes < 50
        ? `<div id="ss-list" class="ss-list"></div>`
        : `<div id="episodes-page-1" class="ss-list ss-list-min ss-list-50" data-page="2"></div>`;

    detailInforContent.insertAdjacentHTML('beforeend', ssList);
  }

  // Main function to call all the others in sequence
  function initializeEpisodeDisplay(totalEpisodes, episodes) {
    addEpisodeListContainer(); // Create the episode list container
    createEpisodeDropdown(totalEpisodes); // First create the dropdown
    attachDropdownListeners(totalEpisodes, episodes); // Then attach event listeners

    // Automatically display the first section of episodes (001-100)
    const start = (selectedDropdownPage - 1) * 100 + 1;
    const end = Math.min(selectedDropdownPage * 100, totalEpisodes);
    displayEpisodesForSection(episodes, start, end);
  }

  // Call the main function after determining totalEpisodes and episodes list
  initializeEpisodeDisplay(totalEpisodes, data.episodes);
}

// Function to update the server list and handle server selection
function updateServerList(subServer1, subServer2, dubServer1, dubServer2) {
  // Alternatively, if you have a server list section, update that with the available servers
  const serversContent = document.querySelector('.player-servers');
  serversContent.innerHTML = `
      <div id="servers-content">
        <div class="ps_-status">
          <div class="content">
            <div class="server-notice">
              <strong>You are watching <b>Episode ${selectedEpisode}</b></strong>

              If current server doesn't work please try other
              servers beside.
            </div>
          </div>
        </div>

        <div class="ps_-block ps_-block-sub servers-sub">
          <div class="ps__-title">
            <i class="fas fa-closed-captioning mr-2"></i>SUB:
          </div>
          <div class="ps__-list">
            <div class="item server-item" data-src="${subServer1}">
              ${
                subServer1 === 'null-page'
                  ? `<a href="javascript:;" class="btn" data-toggle="modal" data-target="#modalcharacters-sub1" data-type="sub" data-index="1">+ADD</a>`
                  : `<a href="javascript:;" class="btn" data-type="sub" data-index="1">SUB-1</a>`
              }
            </div>
            <div class="item server-item" data-src="${subServer2}">
              ${
                subServer2 === 'null-page'
                  ? `<a href="javascript:;" class="btn" data-toggle="modal" data-target="#modalcharacters-sub2" data-type="sub" data-index="2">+ADD</a>`
                  : `<a href="javascript:;" class="btn" data-type="sub" data-index="2">SUB-2</a>`
              }
            </div>
          </div>
          <div class="clearfix"></div>
        </div>

        <div class="ps_-block ps_-block-dub servers-dub">
          <div class="ps__-title">
            <i class="fas fa-microphone-alt mr-2"></i>DUB:
          </div>
          <div class="ps__-list">
            <div class="item server-item" data-src="${dubServer1}">
              ${
                dubServer1 === 'null-page'
                  ? `<a href="javascript:;" class="btn" data-toggle="modal" data-target="#modalcharacters-dub1" data-type="dub" data-index="1">+ADD</a>`
                  : `<a href="javascript:;" class="btn" data-type="dub" data-index="1">DUB-1</a>`
              }
            </div>
            <div class="item server-item" data-src="${dubServer2}">
              ${
                dubServer2 === 'null-page'
                  ? `<a href="javascript:;" class="btn" data-toggle="modal" data-target="#modalcharacters-dub2" data-type="dub" data-index="2">+ADD</a>`
                  : `<a href="javascript:;" class="btn" data-type="dub" data-index="2">DUB-2</a>`
              }
            </div>
          </div>
          <div class="clearfix"></div>
        </div>
      </div>`;

  // Now attach event listeners to the dynamically inserted buttons
  attachServerClickEvents();

  // Automatically select the previously selected server or the first available server
  selectDefaultServer();
}

// Function to attach event listeners to server buttons
function attachServerClickEvents() {
  const serversContent = document.querySelector('.player-servers');
  const serverButtons = serversContent.querySelectorAll('.server-item a');

  serverButtons.forEach(button => {
    button.addEventListener('click', function () {
      const serverItem = this.parentElement;
      const serverSrc = serverItem.getAttribute('data-src');

      // Update the iframe src with the selected server URL
      const playerIframe = document.getElementById('iframe-embed');
      playerIframe.src = serverSrc;

      // Remove 'active' class from any previously active button
      serversContent.querySelectorAll('.server-item a').forEach(btn => {
        btn.classList.remove('active');
      });

      // Add 'active' class to the clicked button
      this.classList.add('active');

      // Store the selected server type and index in localStorage
      selectedServerType = this.getAttribute('data-type');
      selectedServerIndex = this.getAttribute('data-index');
      localStorage.setItem('selectedServerType', selectedServerType);
      localStorage.setItem('selectedServerIndex', selectedServerIndex);
    });
  });
}

// Function to automatically select the previously selected server or fallback to the first one
function selectDefaultServer() {
  const serversContent = document.querySelector('.player-servers');
  const defaultServerSelector = serversContent.querySelector(
    `.btn[data-type="${selectedServerType}"][data-index="${selectedServerIndex}"]`
  );

  if (defaultServerSelector) {
    defaultServerSelector.click(); // Click the default server
  } else {
    // Fallback: select the first available server
    const firstServerSelector = serversContent.querySelector('.btn');
    if (firstServerSelector) {
      firstServerSelector.click();
    } else {
      console.error('No servers available to select');
    }
  }
}

// Function to generate connection HTML and add it to the page
function updateConnections(connections, allAnimeData, currentPage) {
  const connectionWrapper = document.querySelector('.connection-wrapper');
  if (!connectionWrapper) {
    console.error('Connection wrapper element not found!');
    return;
  }

  // Clear existing connections
  connectionWrapper.innerHTML = '';

  // Match connection ids with anime data
  let matchedConnections = connections
    .map(conn => {
      const animeMatch = allAnimeData.find(anime => anime.id === conn.id);
      if (animeMatch) {
        return { ...animeMatch, connectionType: conn.type };
      }
      return null;
    })
    .filter(Boolean);

  // Sort by dateStart (oldest to newest)
  matchedConnections.sort((a, b) => {
    const dateA = new Date(a.dateStart);
    const dateB = new Date(b.dateStart);
    return dateA - dateB;
  });

  // Generate HTML for each matched connection
  matchedConnections.forEach(connection => {
    // Apply "flw-item-active" if the connection's id matches the currentPage
    const isActive = currentPage.includes(connection.id)
      ? 'flw-item-active'
      : '';

    const connectionHTML = `
      <div class="flw-item ${isActive}">
        <div class="film-poster">
          <div class="tick tick-rate">18+</div>
          <div class="tick ltr">
            <div class="tick-item tick-sub">
              <i class="fas fa-closed-captioning mr-1"></i>${
                connection.eposideCount || 0
              }
            </div>
            <div class="tick-item tick-dub">
              <i class="fas fa-microphone mr-1"></i>${
                connection.eposideCount || 0
              }
            </div>
            <div class="tick-item tick-eps">${
              connection.eposideCount || 0
            }</div>
          </div>
          <img data-src="${connection.poster}" src="${
            connection.poster
          }" class="film-poster-img lazyloaded" alt="${connection.animeEnglish}">
          <a href="watch/${
            connection.page
          }" class="film-poster-ahref item-qtip" title="${
            connection.animeEnglish
          }">
            <i class="fas fa-play"></i>
          </a>
        </div>
        <div class="film-detail">
          <h3 class="film-name">
            <a href="page/${connection.page}" title="${
              connection.animeEnglish
            }" class="dynamic-name" data-jname="${connection.animeOriginal}">
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
  });
}

// Fetch the anime data from the endpoint and run the episode list creation
window.onload = function () {
  // Extract the "page" part from the URL (e.g., 'sgt-frog-516.html')
  const currentPage = window.location.pathname
    .split('/')
    .pop()
    .replace('.html', '');
  console.log(`Current page: ${currentPage}`); // Result: 'sgt-frog-516'

  // Wait for the dataReady event to ensure jsonData is populated
  document.addEventListener('dataReady', () => {
    console.log('Data is ready:', jsonData);
    handleFetchedData(jsonData, currentPage);
  });

  // Separate function to handle fetched data
  function handleFetchedData(jsonData, currentPage) {
    const matchingAnime = findPathname(currentPage, jsonData);

    if (matchingAnime.length > 0) {
      console.log('Found matching anime:', matchingAnime[0]);

      const currentEpisode = localStorage.getItem('selectedEpisode') || 1;
      const animeData = matchingAnime[0];

      // Update the UI with the fetched data
      updateAniscDetail(animeData); // Breadcrumb, film name, etc.
      updatePosterImage(animeData); // Poster image
      createEpisodeList(animeData); // Episodes and dropdown

      // Update connections if available
      if (animeData.connections && animeData.connections.length > 0) {
        updateConnections(animeData.connections, jsonData, currentPage);
      }
    } else {
      console.warn('No matching anime found for this page.');
    }
  }

  // Fetch and display recommendations
  fetchAndDisplayRecommendations(currentPage);
};

// Utility function to find the current anime in the JSON data
function findPathname(currentPage, data) {
  return data.filter(anime => anime.page === currentPage);
}
