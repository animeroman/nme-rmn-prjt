"use strict";
import { endpoint } from "./config.js";

const searchData = [];
fetch(endpoint)
  .then((blob) => blob.json())
  .then((data) => searchData.push(...data));

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

function matchWords(inputWords, target) {
  try {
    return inputWords.every((inputWord) => {
      return target
        .split(" ")
        .some((targetWord) => transpositionMatch(inputWord, targetWord));
    });
  } catch (err) {
    throw err;
  }
}

function findMatches(wordToMatch, searchData) {
  try {
    const inputWords = wordToMatch.toLowerCase().split(" ");

    return searchData.filter((place) => {
      const animeEnglishWords = place.animeEnglish.toLowerCase().split(" ");
      const animeOriginalWords = place.animeOriginal.toLowerCase().split(" ");

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
// Old find matches
/*function findMatches(wordToMatch, searchData) {
  return searchData.filter(place => {
    // here we need to figure out if the animeEnglish or animeOriginal matches what was searched
    const regex = new RegExp(wordToMatch, 'gi');
    // return place.animeEnglish.match(regex) || place.animeOriginal.match(regex);
    return (
      transpositionMatch(wordToMatch, place.animeEnglish) ||
      transpositionMatch(wordToMatch, place.animeOriginal)
    );
  });
}*/

function numberWithCommas(x) {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function applyHighlighting(text, input) {
  try {
    let highlightedText = "";
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
  } catch (err) {
    throw err;
  }
}

function displayMatches() {
  try {
    const matchArray = findMatches(this.value, searchData);
    const limitedResults = matchArray.slice(0, 5); // Limit results to 5
    const inputValue = this.value.toLowerCase();

    const html = limitedResults
      .map((place) => {
        let animeID = place.id;
        let animeEnglishName = place.animeEnglish;
        let animeOriginalName = place.animeOriginal;
        let animeDuration = place.duration;
        let animeType = place.type;
        let animeStatus = place.status;
        let animeRated = place.rated;
        let animeScore = place.score;
        let animeSeason = place.season;
        let animeLanguage = place.language;
        let animeDateStart = place.dateStart;
        let animeDateEnd = place.dateEnd;
        let posterLink = place.poster;
        let pageLink = place.page;

        // Apply fuzzy highlighting
        animeEnglishName = applyHighlighting(animeEnglishName, inputValue);
        animeOriginalName = applyHighlighting(animeOriginalName, inputValue);

        return `
      <a href="${pageLink}" class="nav-item">
          <div class="film-poster">
              <img class="film-poster-img lazyloaded" alt="Love♥Love? Specials" src="${posterLink}">
          </div>
          <div class="srp-detail">
              <h3 class="film-name">${animeEnglishName}</h3>
                  <div class="alias-name">${animeOriginalName}</div>
              <div class="film-infor">
                  <span>${animeDateStart}</span><i class="dot"></i>${animeType}<i class="dot"></i><span>${animeDuration}</span>
              </div>
          </div>
          <div class="clearfix"></div>
      </a>
    `;
      })
      .join("");

    resultsContainer.innerHTML = html;

    if (this.value === "") {
      resultsContainer.innerHTML = ""; // Clear the suggestions if input is empty
      return;
    }
  } catch (err) {
    throw err;
  }
}

const searchInput = document.querySelector(".search-input");
const resultsContainer = document.querySelector(".result");
// const suggestions = document.querySelector('.filter-suggestions');

searchInput.addEventListener("change", displayMatches);
searchInput.addEventListener("keyup", displayMatches);
