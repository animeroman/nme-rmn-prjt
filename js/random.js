import { endpoint } from './config.js';

const searchDataEngineRandom = [];
fetch(endpoint)
  .then(blob => blob.json())
  .then(data => {
    searchDataEngineRandom.push(...data);

    // Function to get a random anime object from searchDataEngineRandom
    function getRandomAnime() {
      let randomAnime;

      // Keep trying until a matching anime is found
      do {
        const randomAnimeId = Math.floor(Math.random() * 70000) + 1;
        randomAnime = searchDataEngineRandom.find(
          anime => anime.id == randomAnimeId
        );
      } while (!randomAnime); // Repeat until an anime is found

      return randomAnime;
    }

    // Select the anchor element by ID
    const randomAnimeLink = document.getElementById('random');
    const randomAnimeLink2 = document.getElementById('random2');

    // Add an event listener to the anchor element for the click event
    randomAnimeLink.addEventListener('click', function (event) {
      // Prevent the default action of the anchor element
      event.preventDefault();

      // Get a random anime (this will keep searching until it finds one)
      const randomAnime = getRandomAnime();

      // Navigate to the page link of the found anime
      window.location.href = `https://myanime.com/anime/${randomAnime.page}`;
    });
    randomAnimeLink2.addEventListener('click', function (event) {
      // Prevent the default action of the anchor element
      event.preventDefault();

      // Get a random anime (this will keep searching until it finds one)
      const randomAnime = getRandomAnime();

      // Navigate to the page link of the found anime
      window.location.href = `https://myanime.com/anime/${randomAnime.page}`;
    });
  });
