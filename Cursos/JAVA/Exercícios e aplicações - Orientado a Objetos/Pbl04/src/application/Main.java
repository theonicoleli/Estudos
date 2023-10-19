package application;

import entities.Cliente;
import entities.Funcionario;
import entities.Gerente;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<Cliente> clientes = new ArrayList<>();
        ArrayList<Funcionario> funcionarios = new ArrayList<>();
        ArrayList<Gerente> gerentes = new ArrayList<>();

        System.out.println("Seja bem vindo!");
        do {
            System.out.print("Digite: \n1) Cadastrar pessoa\n2) Listar pessoas\n3) Buscar por tipo\nDigite o valor ao lado: ");
            int option = sc.nextInt();
            if (option == 1) {
                System.out.print("Quantas pessoas deseja cadastrar? ");
                int numeroPessoas = sc.nextInt();
                for (int i = 0; i < numeroPessoas; i++) {
                    System.out.print("Digite: \n1) Cliente\n2) Funcionario\n3) Gerente\nDigite o valor ao lado: ");
                    int newPerson = sc.nextInt();
                    sc.nextLine();
                    System.out.print("Digite seu nome: ");
                    String nome = sc.nextLine();
                    System.out.print("Digite seu peso: ");
                    String peso = sc.nextLine();
                    System.out.print("Digite sua idade: ");
                    int idade = sc.nextInt();
                    if (newPerson >= 2 && newPerson <= 3) {
                        System.out.print("Digite o salário: ");
                        double salario = sc.nextDouble();
                        sc.nextLine();
                        System.out.print("Escreva o setor: ");
                        String setor = sc.nextLine();
                        if (newPerson == 2) {
                            funcionarios.add(new Funcionario(nome, idade, peso, setor, salario));
                        } else {
                            gerentes.add(new Gerente(nome, idade, peso, setor, salario));
                        }
                    } else if (newPerson == 1) {
                        clientes.add(new Cliente(nome, idade, peso));
                    } else {
                        System.out.println("Digite um número válido!");
                    }
                }
            } else if (option == 2) {
                for (Cliente cliente : clientes) {
                    cliente.mostrarCliente();
                }
                for (Funcionario funcionario : funcionarios) {
                    funcionario.mostrarFuncionario();
                }
                for (Gerente gerente : gerentes) {
                    gerente.mostrarGerente();
                }
            } else if (option == 3) {
                System.out.print("Digite: \n1) Cliente\n2) Funcionario\n3) Gerente\nDigite o valor ao lado: ");
                int selectType = sc.nextInt();
                sc.nextLine();
                if (selectType == 1) {
                    System.out.println("Digite o nome: ");
                    String name = sc.nextLine();
                    for (Cliente cliente : clientes) {
                        if (cliente.getNome().equals(name)) {
                            cliente.mostrarCliente();
                        }
                    }
                } else if (selectType == 2) {
                    System.out.println("Digite o nome: ");
                    String name = sc.nextLine();
                    for (Funcionario funcionario : funcionarios) {
                        if (funcionario.getNome().equals(name)) {
                            funcionario.mostrarFuncionario();
                        }
                    }
                } else if (selectType == 3) {
                    System.out.println("Digite o nome: ");
                    String name = sc.nextLine();
                    for (Gerente gerente : gerentes) {
                        if (gerente.getNome().equals(name)) {
                            gerente.mostrarGerente();
                        }
                    }
                }
            } else {
                System.out.println("Digite um número válido!");
            }
        } while (true);
    }
}
