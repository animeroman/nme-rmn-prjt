// prettier-ignore
// export const endpoint = 'https://animeroman.github.io/Source/json/main-search.json';
// export const endpoint = 'http://127.0.0.1:5000/api/anime';
export const endpoint = 'https://apiromanlast.fly.dev/api/anime';
export const jsonData = []; // Global array to store data

export const TIMEOUT_SEC = 10;
export const RES_PER_PAGE = 10;
export const apiKey =
  'SkYCKXd3lZwgW7SDZZBcQOkHoCw4ggczeGFAmtbdUeJFTMWua3KYW9RDw36Esppx1c6Kp6wfy0fTh1YdvUTMF5faEyurPItvRwUKrkiZtT8DMO33yiHEppNcusg85dYC'; // Use the same key as in the backend
export const MODAL_CLOSE_SEC = 2.5;

// Fetch data from the endpoint and populate jsonData
fetch(endpoint)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return response.json(); // Parse the JSON
  })
  .then(data => {
    // Filter out items where "rated" is "Rx"
    const filteredData = data.filter(
      item => item.rated !== 'Rx' && item.rated !== 'R+' && item.rated !== 'R'
    );

    // Populate jsonData with the filtered results
    jsonData.push(...filteredData);

    // Dispatch an event when data is ready
    document.dispatchEvent(new Event('dataReady'));
  })
  .catch(error => {
    console.error('Error fetching the anime data:', error);
  });

/*
export async function fetchAnimeData() {
  try {
    const response = await fetch(endpoint, {
      headers: {
        Authorization: `Bearer ${apiKey}`,
      },
    });

    if (!response.ok) {
      throw new Error(`Failed to fetch: ${response.status}`);
    }

    const jsonData = await response.json();

    // Populate the data array
    data.push(...jsonData);
  } catch (error) {
    console.error('Error fetching anime data:', error);
  }
}

document.addEventListener('DOMContentLoaded', async () => {
  await fetchAnimeData();
  console.log('Fetched anime data:', data);
});
*/

// document.addEventListener("DOMContentLoaded", function() { ... });
