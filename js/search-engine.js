'use strict';
import { jsonData } from './config.js';
import { countEpisodes } from './lister.js';
import { initializeResultCount } from './resultCount.js';

export const resultsPerPage = 48;
let currentPage = 1; // Keep track of the current page
export let totalPages = 0; // Total pages based on the number of results

// Wait for the dataReady event to ensure jsonData is populated
document.addEventListener('dataReady', () => {
  try {
    const keyword = getQueryParam('keyword');
    if (keyword) {
      displayMatches(keyword, currentPage); // Trigger search with the keyword and current page
    }
  } catch (error) {
    throw error;
  }
});

// Function to get query parameter from URL
function getQueryParam(param) {
  try {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
  } catch (error) {
    throw error;
  }
}

function fuzzyMatch(input, target) {
  try {
    input = input.toLowerCase();
    target = target.toLowerCase();

    let inputIndex = 0;
    let targetIndex = 0;

    while (inputIndex < input.length && targetIndex < target.length) {
      if (input[inputIndex] === target[targetIndex]) {
        inputIndex++;
      }
      targetIndex++;
    }

    return inputIndex === input.length; // Return true if all characters in input are matched in target
  } catch (err) {
    throw err;
  }
}

// Transposition match function (for input character swaps)
function transpositionMatch(input, target) {
  try {
    if (fuzzyMatch(input, target)) return true;

    for (let i = 0; i < input.length - 1; i++) {
      let transposed =
        input.slice(0, i) + input[i + 1] + input[i] + input.slice(i + 2);

      if (fuzzyMatch(transposed, target)) return true;
    }

    return false;
  } catch (err) {
    throw err;
  }
}

// Match words with transposition
function matchWords(inputWords, target) {
  try {
    return inputWords.every(inputWord => {
      return target
        .split(' ')
        .some(targetWord => transpositionMatch(inputWord, targetWord));
    });
  } catch (err) {
    throw err;
  }
}

// Find matches based on the input word
export function findMatches(wordToMatch, jsonData) {
  try {
    const inputWords = wordToMatch.toLowerCase().split(' ');

    return jsonData.filter(place => {
      const animeEnglishWords = place.animeEnglish.toLowerCase().split(' ');
      const animeOriginalWords = place.animeOriginal.toLowerCase().split(' ');

      // Check if all input words match any part of the animeEnglish or animeOriginal
      return (
        matchWords(inputWords, place.animeEnglish) ||
        matchWords(inputWords, place.animeOriginal)
      );
    });
  } catch (err) {
    throw err;
  }
}

// Display matches for the search input with pagination
function displayMatches(inputValue, page) {
  try {
    let matchArray;

    // If inputValue is empty or only contains whitespace, show all results
    if (inputValue.trim() === '') {
      matchArray = jsonData; // Use the entire dataset
    } else {
      matchArray = findMatches(inputValue, jsonData);
    }

    totalPages = Math.ceil(matchArray.length / resultsPerPage); // Calculate total pages
    const startIndex = (page - 1) * resultsPerPage;
    const endIndex = startIndex + resultsPerPage;
    const paginatedResults = matchArray.slice(startIndex, endIndex); // Get results for the current page

    const html = paginatedResults
      .map(place => {
        let animeEnglishName = place.animeEnglish;
        let animeOriginalName = place.animeOriginal;
        let animeDuration = place.duration;
        let animeType = place.type;
        let posterLink = place.poster;
        let pageLink = place.page;
        let episode = place.eposideCount;

        const subCount = countEpisodes(place, 'sub'); // Call the function to count sub links
        const dubCount = countEpisodes(place, 'dub'); // Call the function to count dub links
        const rMark =
          place.rated === 'R' || place.rated === 'R+' || place.rated === 'Rx'
            ? `<div class="tick tick-rate">18+</div>`
            : '';

        resultsContainerEngine.insertAdjacentHTML(
          'afterbegin',
          `
      <div class="flw-item flw-item-big">
        <div class="film-poster">
          ${rMark}
          <div class="stick-mask bottom-left">
            <div class="item item-flex item-dub">
              <i class="fas fa-microphone mr-1"></i>${subCount}
            </div>
            <div class="item item-flex item-sub">
              <i class="fas fa-closed-captioning mr-1"></i>${dubCount}
            </div>
          </div>
          <div class="stick-mask bottom-right">
            <div class="tick-item tick-eps">EP: ${episode}</div>
          </div>
          <img data-src="${posterLink}" class="film-poster-img lazyload" src="${posterLink}" />
          <a href="watch/${pageLink}.html" class="film-poster-ahref item-qtip"><i class="fas fa-play"></i></a>
        </div>
        <div class="film-detail">
          <h3 class="film-name">
            <a href="watch/${pageLink}.html" class="dynamic-name" data-jname="${animeOriginalName}">
              ${animeEnglishName}
            </a>
          </h3>
          <div class="description"></div>
          <div class="fd-infor">
            <span class="fdi-item">${animeType}</span>
            <span class="dot"></span>
            <span class="fdi-item fdi-duration">${animeDuration}</span>
          </div>
        </div>
        <div class="clearfix"></div>
      </div>
    `
        );
      })
      .join('');

    updatePagination(page); // Update pagination controls
  } catch (err) {
    throw err;
  }
}

// Update pagination controls
export function updatePagination(currentPage) {
  try {
    const paginationPlace = document.querySelector('.pagination-pages');
    let paginationHTML = '';

    // Calculate the starting and ending page numbers for pagination
    let startPage = Math.max(currentPage - 1, 1); // Start 1 page before current, minimum 1
    let endPage = Math.min(currentPage + 1, totalPages); // End 1 page after current, maximum totalPages

    // Ensure that there are exactly 3 pages displayed (if possible)
    if (endPage - startPage < 2) {
      if (startPage === 1) {
        endPage = Math.min(3, totalPages);
      } else if (endPage === totalPages) {
        startPage = Math.max(totalPages - 2, 1);
      }
    }

    // First page button
    if (currentPage > 1) {
      paginationHTML += `
      <li class="page-item">
        <a title="First" class="page-link" href="#" onclick="goToPage(1)">&laquo;</a>
      </li>`;
    }

    // Previous page button
    if (currentPage > 1) {
      paginationHTML += `
      <li class="page-item">
        <a title="Previous" class="page-link" href="#" onclick="goToPage(${
          currentPage - 1
        })">&lsaquo;</a>
      </li>`;
    }

    // Page numbers (display only 3 pages)
    for (let i = startPage; i <= endPage; i++) {
      if (i === currentPage) {
        paginationHTML += `
        <li class="page-item active"><a class="page-link">${i}</a></li>`;
      } else {
        paginationHTML += `
        <li class="page-item"><a class="page-link" href="#" onclick="goToPage(${i})">${i}</a></li>`;
      }
    }

    // Next page button
    if (currentPage < totalPages) {
      paginationHTML += `
      <li class="page-item">
        <a title="Next" class="page-link" href="#" onclick="goToPage(${
          currentPage + 1
        })">&rsaquo;</a>
      </li>`;
    }

    // Last page button
    if (currentPage < totalPages) {
      paginationHTML += `
      <li class="page-item">
        <a title="Last" class="page-link" href="#" onclick="goToPage(${totalPages})">&raquo;</a>
      </li>`;
    }

    paginationPlace.innerHTML = paginationHTML;
  } catch (err) {
    throw err;
  }
}

// Go to the specified page
function goToPage(page) {
  try {
    currentPage = page;
    const keyword = getQueryParam('keyword'); // Get the current search keyword
    if (keyword) {
      displayMatches(keyword, page); // Display matches for the new page
    }
  } catch (err) {
    throw err;
  }
}

// Initialize search with keyword from URL if present
window.onload = function () {
  const keyword = getQueryParam('keyword'); // Get the keyword from the URL
  if (keyword === null || keyword.trim() === '') {
    // If no keyword, display all animes
    currentPage = 1; // Reset to the first page
    displayMatches('', currentPage);
  } else {
    // If there's a keyword, search as usual
    displayMatches(keyword, currentPage);
  }

  initializeResultCount();
};

const resultsContainerEngine = document.querySelector('.film_list-wrap');
