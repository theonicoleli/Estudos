import java.util.Scanner;

public class Pessoa {
    private String nome;
    private String cpf;
    private int idade;
    private ContaBancaria conta;

    public void adicionarPessoa(String nome, String cpf, int idade){
        this.nome = nome;
        this.cpf = cpf;
        this.idade = idade;
    }

    public void criarContaBancaria() {
        conta = new ContaBancaria();
        conta.numeroContaRandom();
    }

    public String getNome(){
        return this.nome;
    }

    public String getConta(){
        return conta.getnConta();
    }

}
