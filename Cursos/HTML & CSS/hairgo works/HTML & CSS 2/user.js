document.addEventListener("DOMContentLoaded", function() {
    var icon_moon_sun = document.getElementById("icon_moon_sun");
    var container = document.getElementById("container")

    function colorTheme() {
        icon_moon_sun.classList.toggle("fa-moon");
        icon_moon_sun.classList.toggle("fa-sun");
        container.classList.toggle('dark');
    }

    icon_moon_sun.addEventListener("click", colorTheme);
});
