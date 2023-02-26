"use strict";

document
    .querySelectorAll("[data-display-toggle]")
    .forEach(function ($triggerEl) {
        var drawerId = $triggerEl.getAttribute("data-display-toggle");
        var $drawerEl = document.getElementById(drawerId);
        console.log($drawerEl);
        if ($drawerEl) {
            $drawerEl.style.trans
        }
    });
