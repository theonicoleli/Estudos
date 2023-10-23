function meuEscopo() {
    const form = document.querySelector('.form');
    const resultado = document.querySelector('.resultado');

    const pessoas = [];

    form.addEventListener('submit', (evento) => {
        evento.preventDefault();
        
        const nome = document.querySelector('.nome');
        const sobrenome = document.querySelector('.sobrenome');
        const peso = document.querySelector('.peso');
        const altura = document.querySelector('.altura');

        console.log(nome.value, sobrenome.value, peso.valeu, altura.value)

        pessoas.push({
            nome: nome.Value,
            sobrenome: sobrenome.value,
            peso: peso.value,
            altura: altura.value
        });

        resultado.innerHTML += `<p>Nome: ${nome.value}, sobrenome: ${sobrenome.value}, 
        peso: ${peso.value}, altura: ${altura.value}</p>`;
    });

    console.log(pessoas);
}
meuEscopo();
