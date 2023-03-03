"use strict";

var addMissionInput = document.getElementById("mission-input");
var addMissionButton = document.getElementById("mission-add-button");

addMissionInput.addEventListener("keyup", (event) => {
  const result = event.target.value;
  if (result.length > 0) {
    try {
      if (addMissionButton.disabled) addMissionButton.disabled = false;
    } catch (error) {
      console.log(error);
    }
  } else {
    try {
      addMissionButton.disabled = true;
    } catch (error) {
      console.log(error);
    }
  }
});

var auxDateButtons = document.querySelectorAll("a#aux-date-button");
var removeDateButton = document.querySelector("a.removeDateButton");
var auxDateSpan = document.querySelector(
  '[data-dropdown-toggle="aux-date-dropdown"] .aux-value'
);

auxDateButtons.forEach((element) => {
  element.addEventListener("click", (event) => {
    var eValue = element.dataset.value;
    auxDateSpan.textContent = "Son tarih: " + eValue;
    auxDateSpan.classList.remove("hidden");
    removeDateButton.classList.replace("hidden", "flex");
  });
});

removeDateButton.addEventListener("click", (event) => {
  auxDateSpan.classList.add("hidden");
});

addMissionButton.addEventListener("click", (event) => {
  var task_title = addMissionInput.value;
  console.log(task_title);
});