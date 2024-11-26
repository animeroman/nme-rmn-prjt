// Function to count and display the number of 'flw-item' elements in 'film_list-wrap'
function countFlwItems() {
  try {
    // Get the 'film_list-wrap' container
    const filmListWrap = document.querySelector('.film_list-wrap');

    // Check if the container exists
    if (!filmListWrap) {
      console.error("Error: '.film_list-wrap' container not found.");
      return;
    }

    // Count the number of 'flw-item' elements inside the container
    const flwItems = filmListWrap.querySelectorAll('.flw-item');
    const flwItemCount = flwItems.length;

    // Display the count in the 'bah-result' div (assuming it's a class)
    const resultDiv = document.querySelector('.bah-result span');

    // Check if the resultDiv exists
    if (!resultDiv) {
      console.error("Error: '.bah-result span' element not found.");
      return;
    }

    // Update the text content with the number of results
    resultDiv.textContent = `${flwItemCount} results`;

    // Log the count for debugging purposes
    console.log(`${flwItemCount} results found`);
  } catch (error) {
    console.error('Error in countFlwItems:', error);
  }
}

// Use MutationObserver to watch for changes in the DOM
function observeFlwItems() {
  try {
    const filmListWrap = document.querySelector('.film_list-wrap');

    // Check if the container exists
    if (!filmListWrap) {
      console.error("Error: '.film_list-wrap' container not found.");
      return;
    }

    // Create a MutationObserver to monitor changes in the film_list-wrap container
    const observer = new MutationObserver(() => {
      // Whenever a new child is added to the 'film_list-wrap', update the count
      countFlwItems();
    });

    // Start observing the 'film_list-wrap' container for changes in its children
    observer.observe(filmListWrap, { childList: true, subtree: true });

    // Call countFlwItems initially in case the content is already loaded
    countFlwItems();
  } catch (error) {
    console.error('Error in observeFlwItems:', error);
  }
}

// Delayed initialization to ensure data is rendered
function initializeResultCount() {
  // Use MutationObserver to trigger counting after DOM updates
  const waitForContent = setInterval(() => {
    const firstAnimeItem = document.querySelector('.film_list-wrap .flw-item');

    // Check if the first anime item is available
    if (firstAnimeItem) {
      clearInterval(waitForContent); // Stop polling
      observeFlwItems(); // Start observing DOM mutations
      countFlwItems(); // Perform an initial count
    }
  }, 100); // Check every 100ms
}

// Hybrid Initialization: Use both DOMContentLoaded and window.onload
document.addEventListener('DOMContentLoaded', initializeResultCount);

// Backup: Ensure the script works even if content is loaded after window.onload
// window.onload = function () {
//   initializeResultCount();
// };
