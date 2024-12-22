"use strict";

// Function to set the filter based on the specified value
function setFilter(filterValue) {
  console.log("Applying filter for:", filterValue);

  // Select all items that need to be filtered
  const items = document.querySelectorAll(".flw-item");

  items.forEach((item) => {
    // Assuming that the category is stored in an element with class 'fdi-item'
    const category = item.querySelector(".fdi-item").innerText;

    // Check if the item's category matches the filter value
    if (category.toLowerCase() === filterValue.toLowerCase()) {
      item.style.display = ""; // Show matching item
    } else {
      item.style.display = "none"; // Hide non-matching item
    }
  });
}
