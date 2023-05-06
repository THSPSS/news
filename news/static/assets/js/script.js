'use strict';

/**
 * add event on element
 */

const addEventOnElem = function (elem, type, callback) {
  if (!elem) {
    return;
  }

  if (Array.isArray(elem)) {
    for (let i = 0; i < elem.length; i++) {
      if (elem[i] && typeof elem[i].addEventListener === 'function') {
        elem[i].addEventListener(type, callback);
      }
    }
  } else {
    if (typeof elem.addEventListener === 'function') {
      elem.addEventListener(type, callback);
    }
  }
}


  

/**
 * navbar toggle
 */

const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const navbar = document.querySelector("[data-navbar]");
const navbarLinks = document.querySelectorAll("[data-nav-link]");
const overlay = document.querySelector("[data-overlay]");


const toggleNavbar = function () {
    navbar.classList.toggle("active");
    overlay.classList.toggle("active");
  }
  

addEventOnElem(navTogglers, "click", toggleNavbar);

const closeNavbar = function () {
navbar.classList.remove("active");
overlay.classList.remove("active");
}

addEventOnElem(navbarLinks, "click", closeNavbar);
