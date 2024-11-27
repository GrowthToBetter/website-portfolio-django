const navbarNav = document.querySelector(".navbar-nav");
const hamburgerMenu = document.querySelector("#hamburger-menu");

document.querySelector("#hamburger-menu").onclick = () => {
  navbarNav.classList.toggle("active");
};

document.addEventListener("click", function (e) {
  if (!hamburgerMenu.contains(e.target) && !navbarNav.contains(e.target)) {
    navbarNav.classList.remove("active");
  }
});

const Context = document.querySelector(".context");
const displayContact = document.querySelector("#Contact");
const MediaQuery = window.matchMedia("(max-width:750px)");

function handlingMediaQuery(event) {

  if (event.matches) {
    displayContact.onclick = () => {
      window.open("/Contact", "_blank");
    };
  } else {
    displayContact.onclick = () => {
      Context.classList.toggle("active");
    };
  }
}

handlingMediaQuery(MediaQuery);

MediaQuery.addEventListener("change", (event) => {
  handlingMediaQuery(event);
});
