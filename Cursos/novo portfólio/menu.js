document.addEventListener('DOMContentLoaded', function() {
    const toggleBtn = document.querySelector('.toggle_btn');
    const dropDownMenu = document.querySelector('.dropdown_menu');
    const toggleBtnIcon = toggleBtn.querySelector('i');

    toggleBtn.addEventListener('click', function(){
    toggleBtn.classList.toggle('open');
    dropDownMenu.classList.toggle('open')
    toggleBtnIcon.classList.toggle('fa-bars');
    toggleBtnIcon.classList.toggle('fa-times');

    if (toggleBtn.classList.contains('open')) {
        dropDownMenu.style.display = 'block';
    } else {
        dropDownMenu.style.display = 'none';
    }
    });
});
