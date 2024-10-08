'use strict';
// JSON data point
const endpoint = 'https://animeroman.github.io/Source/json/search.json';

// Store the selected server type globally to remember it across episodes
let selectedServerType = localStorage.getItem('selectedServerType') || 'sub'; // Default to 'sub'
let selectedServerIndex = localStorage.getItem('selectedServerIndex') || 1; // Default to 'SUB-1' or 'DUB-1'
let selectedEpisode = localStorage.getItem('selectedEpisode') || 1; // Default to Episode 1

// Search.json example
/*
{
    "animeEnglish": "Love, Chunibyo & Other Delusions!",
    "animeOriginal": "Love, Chunibyo & Other Delusions!",
    "duration": "24m",
    "type": "TV",
    "date": "Oct 4, 2012",
    "poster": "https://cdn.noitatnemucod.net/thumbnail/300x400/100/45a469c51892b3a73268c6f4001759d8.jpg",
    "page": "0-firstsubfolder",
    "subCount": "5",
    "dubCount": "5",
    "episodes": [
      {
        "episodeNumber": 1,
        "title": "Episode 1 Title",
        "dubServer1": "#",
        "dubServer2": "#",
        "subServer1": "#",
        "subServer2": "#"
      },
      {
        "episodeNumber": 2,
        "title": "Episode 2 Title",
        "dubServer1": "#",
        "dubServer2": "#",
        "subServer1": "#",
        "subServer2": "#"
      },
      {
        "episodeNumber": 3,
        "title": "Episode 3 Title",
        "dubServer1": "#",
        "dubServer2": "#",
        "subServer1": "#",
        "subServer2": "#"
      },
      {
        "episodeNumber": 4,
        "title": "Episode 4 Title",
        "dubServer1": "#",
        "dubServer2": "#",
        "subServer1": "#",
        "subServer2": "#"
      },
*/
// Add this variable before the loop to track the count of episodes
let totalEpisodes = 0;

let allEpisode = [];

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
    const eposideLabelContent = document.querySelector('.ssc-label');
    const seasonBlockContent = document.querySelector('.seasons-block');

    if (totalEpisodes > 100) {
      seasonBlockContent.classList.add('seasons-block-max');

      let html = `
      <div
        class="ssc-name"
        data-toggle="dropdown"
        aria-haspopup="true"
        aria-expanded="false"
      >
        <i class="fas fa-list mr-3"></i
        ><span id="current-page">EPS: 001-100</span
        ><i class="fas fa-angle-down ml-2"></i>
      </div>
      <div
        class="dropdown-menu dropdown-menu-model"
        aria-labelledby="ssc-list"
      >
    `;

      // Generate dropdown items for every 100 episodes
      for (let i = 0; i < Math.ceil(totalEpisodes / 100); i++) {
        const start = i * 100 + 1;
        const end = Math.min((i + 1) * 100, totalEpisodes);
        const isActive = i === 0 ? 'active' : ''; // Make the first item active by default
        const checkIcon = i === 0 ? 'inline' : 'none'; // Show check icon for the first item
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
    console.log(
      `Displaying episodes from ${start} to ${end}`,
      filteredEpisodes
    ); // Debugging

    if (filteredEpisodes.length === 0) {
      container.innerHTML = '<p>No episodes available for this section.</p>';
      return;
    }

    filteredEpisodes.forEach(episode => {
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
          <div
            class="ep-name e-dynamic-name"
            title="${episode.title}"
          >
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
  }

  // Function to attach click event listeners to dropdown items
  function attachDropdownListeners(totalEpisodes, episodes) {
    const dropdownItems = document.querySelectorAll('.ep-page-item');

    dropdownItems.forEach((item, index) => {
      item.addEventListener('click', function() {
        const currentPageText = this.textContent.trim();
        document.getElementById('current-page').textContent = currentPageText;

        // Remove active state from all items and add to clicked one
        dropdownItems.forEach(el => {
          el.querySelector('i').style.display = 'none';
          el.classList.remove('active');
        });
        this.querySelector('i').style.display = 'inline';
        this.classList.add('active');

        // Get the start and end episode range for the clicked section
        const start = index * 100 + 1;
        const end = Math.min((index + 1) * 100, totalEpisodes);

        // Display episodes for the selected section
        displayEpisodesForSection(episodes, start, end);
      });
    });

    // Automatically display the first section when the page loads (001-100)
    displayEpisodesForSection(episodes, 1, Math.min(100, totalEpisodes));
  }

  // Main function to call all the others in sequence
  function initializeEpisodeDisplay(totalEpisodes, episodes) {
    createEpisodeDropdown(totalEpisodes); // First create the dropdown
    attachDropdownListeners(totalEpisodes, episodes); // Then attach event listeners

    // Manually trigger displaying the first section of episodes (001-100)
    displayEpisodesForSection(episodes, 1, Math.min(100, totalEpisodes));
  }

  // Call the main function after determining totalEpisodes and episodes list
  initializeEpisodeDisplay(totalEpisodes, data.episodes);

  // Add ssList only once
  if (totalEpisodes < 50) {
    const ssList = `
      <div id="ss-list" class="ss-list"></div>
      `;
    //   detailInforContent.innerHTML += ssList;
    detailInforContent.insertAdjacentHTML('beforeend', ssList);
  } else if (totalEpisodes >= 50) {
    const ssList = `
      <div
          id="episodes-page-1"
          class="ss-list ss-list-min ss-list-50"
          data-page="2"
          style=""
      ></div>
      `;
    //detailInforContent.innerHTML += ssList;
    detailInforContent.insertAdjacentHTML('beforeend', ssList);
  }

  // Select the created ssList (after inserting it)
  const container = document.querySelector('.ss-list');

  data.episodes.forEach(episode => {
    // If the number count of episodes is less than 50, use 'episodeHTML'
    if (totalEpisodes < 50) {
      const isActive = episode.episodeNumber == selectedEpisode ? 'active' : ''; // Mark active episode
      const episodeHTML = `
          <a
            title="Episode ${episode.episodeNumber}"
            class="ssl-item ep-item ${isActive}"
            data-number="${episode.episodeNumber}"
            data-subserver1="${episode.subServer1}"
            data-subserver2="${episode.subServer2}"
            data-dubserver1="${episode.dubServer1}"
            data-dubserver2="${episode.dubServer2}"
            href="javascript:;"
          >
            <div class="ssli-order">${episode.episodeNumber}</div>
            <div class="ssli-detail">
              <div
                class="ep-name e-dynamic-name"
                data-jname="${data.animeOriginal}"
                title="${data.animeEnglish}"
              >
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
      // Add to the first container
      //container.innerHTML += episodeHTML;
      container.insertAdjacentHTML('beforeend', episodeHTML);

      // Else if the number of episodes is equal or more than 50, use 'episodeHTML50'
    } else if (totalEpisodes >= 50) {
      const isActive = episode.episodeNumber == selectedEpisode ? 'active' : ''; // Mark active episode

      // Only include episodes with episodeNumber <= 100
      // if (episode.episodeNumber <= 100) {
      if (1 === 1) {
        const episodeHTML = `
          <a
            title="Episode ${episode.episodeNumber}"
            class="ssl-item ep-item ${isActive}"
            data-number="${episode.episodeNumber}"
            data-subserver1="${episode.subServer1}"
            data-subserver2="${episode.subServer2}"
            data-dubserver1="${episode.dubServer1}"
            data-dubserver2="${episode.dubServer2}"
            href="javascript:;"
          >
            <div
              class="ssli-order"
              title="${data.animeEnglish}"
            >
              ${episode.episodeNumber}
            </div>
            <div class="ssli-detail">
              <div
                class="ep-name e-dynamic-name"
                data-jname="${data.animeOriginal}"
                title="${data.animeEnglish}"
              >
                ${data.animeEnglish}
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
        // Add to the second container
        //container.innerHTML += episodeHTML;
        container.insertAdjacentHTML('beforeend', episodeHTML);
      }
    }
  });
  // Add click event listener to each episode link
  const episodeLinks = container.querySelectorAll('.ep-item');
  episodeLinks.forEach(link => {
    link.addEventListener('click', function() {
      // Get server URLs from the clicked element's data attributes
      const subServer1 = this.getAttribute('data-subserver1');
      const subServer2 = this.getAttribute('data-subserver2');
      const dubServer1 = this.getAttribute('data-dubserver1');
      const dubServer2 = this.getAttribute('data-dubserver2');
      const episodeNumber = this.getAttribute('data-number');

      // Store the selected episode in localStorage
      localStorage.setItem('selectedEpisode', episodeNumber);

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

  // Simulate click on the previously selected episode (or the first episode if none was selected)
  const selectedEpisodeElement = container.querySelector(
    `.ep-item[data-number="${selectedEpisode}"]`
  );
  if (selectedEpisodeElement) {
    selectedEpisodeElement.click(); // Automatically load the previously selected episode
  }
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
            <div
              class="item server-item"
              data-src="${subServer1}"
            >
              <a href="javascript:;" class="btn" data-type="sub" data-index="1">SUB-1</a>
            </div>

            <div
              class="item server-item"
              data-src="${subServer2}"
            >
              <a href="javascript:;" class="btn" data-type="sub" data-index="2">SUB-2</a>
            </div>

          </div>
          <div class="clearfix"></div>
        </div>

        <div class="ps_-block ps_-block-sub servers-dub">
          <div class="ps__-title">
            <i class="fas fa-microphone-alt mr-2"></i>DUB:
          </div>

          <div class="ps__-list">
            <div
              class="item server-item"
              data-src="${dubServer1}"
            >
              <a href="javascript:;" class="btn" data-type="dub" data-index="1">DUB-1</a>
            </div>

            <div
              class="item server-item"
              data-src="${dubServer2}"
            >
              <a href="javascript:;" class="btn" data-type="dub" data-index="2">DUB-2</a>
            </div>      
          </div>
          <div class="clearfix"></div>
        </div>
      </div>
          `;
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
    button.addEventListener('click', function() {
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

// Fetch the anime data from the endpoint and run the episode list creation
window.onload = function() {
  // Step 1: Extract the "page" part from the URL (e.g., '0-firstsubfolder.html')
  const currentPage = window.location.pathname
    .split('/')
    .pop()
    .replace('.html', '');
  console.log(`Current page: ${currentPage}`); // Result: '0-firstsubfolder'

  // Step 2: Fetch data from the JSON endpoint
  const anime = [];
  fetch(endpoint)
    .then(blob => blob.json())
    .then(data => {
      anime.push(...data); // Push the fetched data into the 'anime' array

      // Step 3: Find the anime data that matches the current page after data is fetched
      const matchingAnime = findPathname(currentPage, anime);

      if (matchingAnime.length > 0) {
        // Step 4: If a match is found, pass the anime data to createEpisodeList
        createEpisodeList(matchingAnime[0]); // Pass the first match
      } else {
        console.error('No matching anime found for the current page');
      }
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    });

  function findPathname(pathToMatch, anime) {
    return anime.filter(ani => {
      const regex = new RegExp(pathToMatch, 'gi');
      return ani.page.match(regex);
    });
  }
};
