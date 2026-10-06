// Mobile menu toggle
const navToggle = document.getElementById("navToggle");
const siteNav = document.getElementById("siteNav");

if (navToggle && siteNav) {
    navToggle.addEventListener("click", () => {
        const isOpen = siteNav.classList.toggle("open");
        navToggle.setAttribute("aria-expanded", isOpen);
    });

    siteNav.querySelectorAll(".nav-link").forEach((link) => {
        link.addEventListener("click", () => {
            siteNav.classList.remove("open");
            navToggle.setAttribute("aria-expanded", "false");
        });
    });
}

// Highlight the active section in the nav while scrolling
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".nav-link");

const highlightNav = () => {
    let current = sections[0] ? sections[0].id : "";

    sections.forEach((section) => {
        const top = section.offsetTop - 90;
        if (window.scrollY >= top) {
            current = section.id;
        }
    });

    navLinks.forEach((link) => {
        link.classList.toggle("active", link.getAttribute("href") === `#${current}`);
    });
};

window.addEventListener("scroll", highlightNav);
window.addEventListener("load", highlightNav);
