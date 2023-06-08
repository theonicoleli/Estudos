var click_count = 0;

document.addEventListener("mousedown", function(e) {
    var icon_up_arrow = document.getElementById("up_arrow");
    var tela_secundaria = document.getElementById("tela_secundaria");
    var frase_dentro = document.getElementById("frase_dentro");
    var sobre_mim = document.getElementById("sobre_mim");

    function iconArrowStatic() {
        switch(e.which) {
            case 1: 
                console.log("Botão esquerdo");
                if (e.target === icon_up_arrow && e.buttons === 1 && e.type === 'mousedown') {
                    icon_up_arrow.classList.remove("fa-bounce");
                    if (click_count % 2 === 0) {
                        icon_up_arrow.classList.remove("fa-arrow-up");
                        icon_up_arrow.classList.add("fa-arrow-down");
                        sobre_mim.style.display = 'flex';
                        frase_dentro.textContent = "Aperte aqui para retornar ao menu principal";
                    } else {
                        icon_up_arrow.classList.remove("fa-arrow-down");
                        icon_up_arrow.classList.add("fa-arrow-up");
                        sobre_mim.style.display = 'none';
                        frase_dentro.textContent = "Aperte para mais informações";
                    }
                    icon_up_arrow.classList.add("fa-bounce");
                    tela_secundaria.classList.toggle('informationUp');
                    click_count++;
                }
                break;
            default:
                icon_up_arrow.classList.add("fa-bounce");
                break;
        }
    }

    iconArrowStatic();
});
