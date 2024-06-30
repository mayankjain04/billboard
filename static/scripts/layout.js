document.getElementById("scrollBottom").onclick = function () {
    window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
};
// this script is for swithing themes/darkmode
document.addEventListener('DOMContentLoaded', (event) => {
    var theme = document.getElementById("theme")
    var themeSwitch = document.querySelectorAll(".theme-toggle")

    if (localStorage.getItem("darkMode") === 'true') {
        theme.href = "static/dark.css";
        themeSwitch.forEach(function (s) {
            s.checked = true;
            document.querySelectorAll('.theme-icon').forEach(icon => {
                icon.classList.add('bi-moon')
                icon.classList.remove('bi-sun')
            });
        });
    } else {
        theme.href = "static/light.css";
        themeSwitch.forEach(function (s) {
            s.checked = false;
            document.querySelectorAll('.theme-icon').forEach(icon => {
                icon.classList.add('bi-sun')
                icon.classList.remove('bi-moon')
            });

        });
    }

    themeSwitch.forEach(switchInstance => {
        switchInstance.addEventListener('change', function () {
            const isChecked = this.checked;

            if (isChecked) {
                theme.href = "static/dark.css";
                localStorage.setItem('darkMode', 'true');
                themeSwitch.forEach(function (s) {
                    s.checked = true;
                    document.querySelectorAll('.theme-icon').forEach(icon => {
                        icon.classList.remove('custom-show');
                        setTimeout(() => {
                            icon.classList.replace('bi-sun', 'bi-moon')
                            icon.classList.add('custom-show');
                        }, 250);
                    });
                });
            } else {
                theme.href = "static/light.css";
                localStorage.setItem('darkMode', 'false');
                themeSwitch.forEach(function (s) {
                    s.checked = false;
                    document.querySelectorAll('.theme-icon').forEach(function (icon) {
                        icon.classList.remove('custom-show');
                        setTimeout(() => {
                            icon.classList.replace('bi-moon', 'bi-sun')
                            icon.classList.add('custom-show');
                        }, 250);
                    });
                });
            }
        });
    });
});
// this is for adding active class to active navbar links
document.addEventListener('DOMContentLoaded', (event) => {
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === '/' && currentLocation === '/') {
            link.classList.add('active');
        } else if (href.startsWith(currentLocation) && currentLocation !== '/') {
            link.classList.add('active');
        }
    });
});

// this is for tooltips
document.addEventListener("DOMContentLoaded", function() {
    var tooltipElementOne = document.querySelectorAll('.theme-tooltip');
    tooltipElementOne.forEach(function (element) {
        var title = 'Darkmode'; 
        new bootstrap.Tooltip(element, {
            placement: 'bottom',
            fallbackPlacements: ['bottom-start', 'bottom-end', 'top', 'right', 'left'],
            title: title,
        });
    });
    var tooltipElementTwo = document.querySelectorAll('.bi-person');
    tooltipElementTwo.forEach(function (element) {
        var title = 'Profile'; 
        new bootstrap.Tooltip(element, {
            placement: 'right',
            fallbackPlacements: [ 'bottom', 'bottom-start', 'bottom-end', 'top', 'right', 'left'],
            title: title,
        });
    });
});

