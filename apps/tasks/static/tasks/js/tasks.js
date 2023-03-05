"use strict";

// Değişkenler
var addMissionInput = document.getElementById("mission-input");
var addMissionButton = document.getElementById("mission-add-button");
var auxDateButtons = document.querySelectorAll("a.aux-date-button");
var removeDateButton = document.querySelector("a.removeDateButton");
var auxDateSpan = document.querySelector(
  '[data-dropdown-toggle="aux-date-dropdown"] .aux-value'
);

// Yeni görev oluşturma fonksiyonu
function TaskCreateRequest() {
  var exp_date = auxDateSpan.getAttribute("data-value");
  var csrfToken = $("[name=\"csrfmiddlewaretoken\"]").val();
  var postData = {
    title: addMissionInput.value,
    expiration_date: exp_date,
    csrfmiddlewaretoken: csrfToken
  }
  const url = "/tasks/create/"
  $.ajax({
    type: "POST",
    url: url,
    data: postData,
    success: function (response) {
      console.log(response);
    }
  });
}

addMissionInput.addEventListener("keyup", (event) => {
  // keyup Enter tespiti ve TaskCreateRequest 'yönlendirmesi
  if (event.key === "Enter") {
    TaskCreateRequest();
    return;
  }
  // Input value uzunluğu kontrolü ile submit button status değişikliği 
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

// Görev son tarih için dynamic span text
auxDateButtons.forEach((element) => {
  element.addEventListener("click", (event) => {
    var eValue = element.dataset.value;
    auxDateSpan.textContent = "Son tarih: " + eValue;
    auxDateSpan.setAttribute("data-value", eValue);
    auxDateSpan.classList.remove("hidden");
    removeDateButton.classList.replace("hidden", "flex");
  });
});

// Kaldır, görev son tarih
removeDateButton.addEventListener("click", (event) => {
  auxDateSpan.removeAttribute("data-value");
  auxDateSpan.classList.add("hidden");
});

// Click event, submit create button
addMissionButton.addEventListener("click", (event) => {
  TaskCreateRequest();
});