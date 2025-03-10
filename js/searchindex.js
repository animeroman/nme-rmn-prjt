'use strict';
import { jsonData } from './config.js';

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
  } catch (error) {
    console.log(error);
  }
}

function transpositionMatch(input, target) {
  try {
    if (fuzzyMatch(input, target)) return true;

    for (let i = 0; i < input.length - 1; i++) {
      let transposed =
        input.slice(0, i) + input[i + 1] + input[i] + input.slice(i + 2);

      if (fuzzyMatch(transposed, target)) return true;
    }

    return false;
  } catch (error) {
    console.log(error);
  }
}

function matchWords(inputWords, target) {
  try {
    return inputWords.every(inputWord => {
      return target
        .split(' ')
        .some(targetWord => transpositionMatch(inputWord, targetWord));
    });
  } catch (error) {
    console.log(error);
  }
}

function findMatches(wordToMatch, jsonData) {
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
  } catch (error) {
    console.log(error);
  }
}

function numberWithCommas(x) {
  try {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  } catch (error) {
    console.log(error);
  }
}

function applyHighlighting(text, input) {
  try {
    let highlightedText = '';
    let inputIndex = 0;

    for (let i = 0; i < text.length; i++) {
      if (
        inputIndex < input.length &&
        text[i].toLowerCase() === input[inputIndex].toLowerCase()
      ) {
        // Highlight the character and move to the next input character
        highlightedText += `<span class="hl">${text[i]}</span>`;
        inputIndex++;
      } else {
        highlightedText += text[i];
      }

      // If all input characters have been matched, append the rest of the text as is
      if (inputIndex === input.length) {
        highlightedText += text.slice(i + 1);
        break;
      }
    }

    // If input characters remain unmatched, just return the highlighted text
    return highlightedText;
  } catch (error) {
    console.log(error);
  }
}

function displayMatches() {
  try {
    const matchArray = findMatches(this.value, jsonData);
    const limitedResults = matchArray.slice(0, 5); // Limit results to 5
    const inputValue = this.value.toLowerCase();

    const html = limitedResults
      .map(place => {
        let animeEnglishName = place.animeEnglish;
        let animeOriginalName = place.animeOriginal;
        let animeDuration = place.duration;
        let animeType = place.type;
        let animeDate = place.date;
        let posterLink = place.poster;
        let pageLink = place.page;

        // Apply fuzzy highlighting
        animeEnglishName = applyHighlighting(animeEnglishName, inputValue);
        animeOriginalName = applyHighlighting(animeOriginalName, inputValue);

        return `
      <a href="${pageLink}" class="roman-nav-item">
        <div class="roman-film-poster">
            <img class="roman-film-poster-img roman-ls-is-cached lazyloaded" src="${posterLink}">
        </div>
        <div class="roman-srp-detail">
            <h3 class="roman-film-name">${animeEnglishName}</h3>
            
                <div class="roman-alias-name">${animeOriginalName}</div>
            
            <div class="film-infor">
                <span>${animeDate}</span><i class="roman-dot"></i>${animeType}<i class="roman-dot"></i><span>${animeDuration}</span>
            </div>
        </div>
        <div class="clearfix"></div>
      </a>
    `;
      })
      .join('');

    resultsContainer.innerHTML = html;

    if (this.value === '') {
      resultsContainer.innerHTML = ''; // Clear the suggestions if input is empty
      return;
    }
  } catch (error) {
    console.log(error);
  }
}

const searchInput = document.querySelector('.search-input');
const resultsContainer = document.querySelector('.suggestion-place');
// const suggestions = document.querySelector('.filter-suggestions');

searchInput.addEventListener('change', displayMatches);
searchInput.addEventListener('keyup', displayMatches);
