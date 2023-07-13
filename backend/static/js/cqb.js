document.addEventListener("DOMContentLoaded", function () {
  setTimeout(function () {
    document.querySelector("#Alarms").remove();
  }, 4000);
});

function HideAlert() {
  document.querySelector("#alert").remove();
}

function BlockButton() {
  document.querySelector("#block").etAttribute("disabled", "true");
}

var menuButton = document.getElementById("dropdownmenuButton");
menuButton.addEventListener("click", function () {
  var menu = document.getElementById("dropdownmenu");
  if (menu.style.display === "none") {
    menu.style.display = "block";
  } else {
    menu.style.display = "none";
  }
});

var tootlipButton = document.getElementById("tooltip-button");
tootlipButton.addEventListener("click", function () {
  var menu = document.getElementById("tooltip-content");
  if (menu.style.display === "none") {
    menu.style.display = "block";
  } else {
    menu.style.display = "none";
  }
});

var depozitButton = document.getElementById("deposit");
var lideposit = document.getElementById("lideposit");
var liwithdraw = document.getElementById("liwithdraw");
var depozit_menu = document.getElementById("deposit-content");
var withdrawButton = document.getElementById("withdraw");
var withdraw_menu = document.getElementById("withdraw-content");
depozitButton.addEventListener("click", function () {
  if (depozit_menu.style.display === "none") {
    depozit_menu.style.display = "block";
    lideposit.classList.add("is-active");
    withdraw_menu.style.display = "none";
    liwithdraw.classList.remove("is-active");
  } else {
    depozit_menu.style.display = "none";
    lideposit.classList.remove("is-active");
    withdraw_menu.style.display = "block";
    liwithdraw.classList.add("is-active");
  }
});

withdrawButton.addEventListener("click", function () {
  if (withdraw_menu.style.display === "none") {
    withdraw_menu.style.display = "block";
    liwithdraw.classList.add("is-active");
    depozit_menu.style.display = "none";
    lideposit.classList.remove("is-active");
  } else {
    withdraw_menu.style.display = "none";
    liwithdraw.classList.remove("is-active");
    depozit_menu.style.display = "block";
    lideposit.classList.add("is-active");
  }
});
