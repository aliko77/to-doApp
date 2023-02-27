"use strict";

const sidebarButton = document.getElementById('sidebar-button');

sidebarButton.addEventListener("click", () => {
    const buttonTarget = sidebarButton.getAttribute('aria-controls');
    const sidebar = document.getElementById(buttonTarget);
    if (sidebar) {
        sidebar.classList.toggle('-translate-x-full')
    }
});