// this jquery code is for alert
$(document).ready(function () {
    window.setTimeout(function () {
        $(".alert").alert('close');
    }, 15000);
});

// this code is for strollTop
document.getElementById("scrollTop").onclick = function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
};

