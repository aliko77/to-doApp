"use strict";

var addMissionInput = document.getElementById('mission-input');
var addMissionButton = document.getElementById('mission-add-button');

addMissionInput.addEventListener("keyup", (event) => {
    const result = event.target.value
    if (result.length > 0) {
        try {
            if (addMissionButton.disabled)
                addMissionButton.disabled = false
        } catch (error) {
            console.log(error);
        }
    } else {
        try {
            addMissionButton.disabled = true
        } catch (error) {
            console.log(error);
        }
    }
});