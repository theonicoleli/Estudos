package application;

import entities.Calca;
import entities.Camisa;
import entities.Roupa;
import entities.Vestido;

import java.util.ArrayList;

public class Program {

    public static void main(String[] args) {

        ArrayList<Roupa> roupas = new ArrayList<>();

        String nome = "Théo";
        String marca = "Nike";
        String tamanho = "Médio";
        String cor = "Yellow";
        double preco = 45.99;

        Roupa camisa = new Camisa(nome, marca, tamanho, cor, preco);
        Roupa vestido = new Vestido(nome, marca, tamanho, cor, preco);
        Roupa calca = new Calca(nome, marca, tamanho, cor, preco);

        roupas.add(camisa);
        roupas.add(vestido);
        roupas.add(calca);

        for (Roupa roupa: roupas) {
            String classe = null;
            if (roupa instanceof Camisa) {
                classe = "Camisa";
            } else if (roupa instanceof Vestido) {
                classe = "Vestido";
            } else if (roupa instanceof Calca) {
                classe = "Calça";
            }
            System.out.println("Classe: " + classe + ", " + roupa.toString());
        }

    }
}