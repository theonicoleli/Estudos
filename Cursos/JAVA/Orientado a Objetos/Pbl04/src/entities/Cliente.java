package entities;

import java.util.Scanner;

public class Cliente extends Pessoa{

    public Cliente(String nome, int idade, String peso) {
        super(nome, idade, peso);
    }

    public void mostrarCliente() {
        System.out.println("Nome: " + getNome() + "\nIdade: " + getIdade() +
                "\nPeso: " + getPeso());
    }

}
