//Criação de Promessas

const myPromise = new Promise ((resolve, reject) => {

    const nome = 'Théo';

    if(nome === 'Théo'){
        resolve('Usuário Théo, encontrado!')
    } else {
        reject('O úsuario Théo, não foi encontrado.')
    }

});


myPromise.then((data) => {
    console.log(data);
})


//Encadeamento de then's

const myPromise2 = new Promise ((resolve, reject) => {

    const nome = 'Théo';

    if(nome === 'Théo'){
        resolve('Usuário Théo, encontrado!')
    } else {
        reject('O úsuario Théo, não foi encontrado.')
    }

});


myPromise2
    .then((data) => {
        return data.toLowerCase();
    })
    .then((stringModificada) => {
        console.log(stringModificada);
    })


// Retorno Catch

const myPromise3 = new Promise ((resolve, reject) => {

    const nome = 'João';

    if(nome === 'Théo'){
        resolve('Usuário Théo, encontrado!')
    } else {
        reject('O úsuario Théo, não foi encontrado.')
    }

});


myPromise3
    .then((data) => {
        console.log(data);
    })
    .catch((err) => {
        console.log("Erro: " + err)
    })


//Resolver várias promessas

const p1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('P1, OK! Timeout');
    }, 2000)
});

const p2 = new Promise((resolve, reject) => {
    resolve('P2, OK!');
});

const p3 = new Promise((resolve, reject) => {
    resolve('P3, OK!');
});


const resolveAll = Promise.all([p1, p2, p3]).then((data) => {
    console.log(data);
}).catch((err) => {
    console.log("Erro: " + err);
});


//Várias promessas race

const p4 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('P4, OK! Timeout');
    }, 2000)
});

const p5 = new Promise((resolve, reject) => {
    resolve('P5, OK!');
});

const p6 = new Promise((resolve, reject) => {
    resolve('P6, OK!');
});


const resolveAllRace = Promise.race([p4, p5, p6]).then((data) => {
    console.log(data);
}).catch((err) => {
    console.log("Erro: " + err);
});


// Fetch request na API do GitHub
// Fetch API

const userName = 'theonicoleli'

fetch(`https://api.github.com/users/${userName}`, {
    method: 'GET',
    headers: {
        Accept: 'application/vnd.github.v3+json',
    },
}).then((resposta) => {
    console.log(typeof resposta);
    console.log(resposta);
    return resposta.json();
}).then((dados) => {
    console.log(dados);
    console.log(`O nome do usuario é: ${dados.name}`)
}).catch((err) => {
    console.log(`Ocorreu um erro ao tentar encontrar: ${err}`)
})