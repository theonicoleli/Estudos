document.addEventListener("DOMContentLoaded", function() {
    var icon_moon_sun = document.getElementById("icon_moon_sun");
    var forma_geral_color = document.getElementById("forma_geral");

    function colorTheme() {
        icon_moon_sun.classList.toggle("fa-moon");
        icon_moon_sun.classList.toggle("fa-sun");
        forma_geral_color.classList.toggle('dark');
    }

    icon_moon_sun.addEventListener("click", colorTheme);
});
