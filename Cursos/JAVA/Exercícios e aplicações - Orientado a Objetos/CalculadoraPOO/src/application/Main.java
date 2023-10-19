package application;

import entities.Calculadora;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> numeros = new ArrayList<>();
        for (int i = 1; i < 12; i++) {
            numeros.add(i);
        }

        Calculadora calculadora = new Calculadora();
        System.out.println(calculadora.somar(10, 77));
        System.out.println(calculadora.dividir(80, 55));
        System.out.println(calculadora.dividir(numeros));
        System.out.println(calculadora.somar(numeros));
        System.out.println(calculadora.subtrair(66, 7));
        System.out.println(calculadora.subtrair(numeros));
        System.out.println(calculadora.multiplicar(5, 4));
        System.out.println(calculadora.multiplicar(numeros, 2));
    }
}
