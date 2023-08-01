function validate() {
    const dataNascimento = cadastro.nascimento.value;
    const dataNascimentoCliente = new Date(dataNascimento);
    const dataAtual = new Date();
    const anoNascimentoCliente = dataNascimentoCliente.getFullYear();
    const mesNascimentoCliente = dataNascimentoCliente.getMonth();
    const diaNascimentoCliente = dataNascimentoCliente.getDate();
    
    if (dataNascimentoCliente > dataAtual) {
        alert("Data de nascimento inválida. Verifique se a data está correta.");
        return;
    }

    let idadeCliente = dataAtual.getFullYear() - anoNascimentoCliente;
    
    if (dataAtual.getMonth() < mesNascimentoCliente || 
        (dataAtual.getMonth() === mesNascimentoCliente && dataAtual.getDate() < diaNascimentoCliente)) {
        idadeCliente--;
    }

    if (cadastro.nome.value === "") {
        alert("Digite as informações necessárias.");
    } else if (dataNascimento === "") {
        alert("Digite sua data de nascimento.");
    } else if (cadastro.sexo.value === "nenhum") {
        alert("Selecione seu sexo.");
    } else if (cadastro.funcao.value === "nenhum") {
        alert("Selecione sua função.");
    } else if (cadastro.atuacao.value === "nenhum") {
        alert("Selecione sua atuação.");
    } else if (idadeCliente < 18) {
        alert("Para se candidatar você precisa ter 18 anos ou mais!");
    }
}