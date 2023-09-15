package entities;

import java.util.ArrayList;
import java.util.Collections;

public class Calculadora {

    public Calculadora(){
    }

    public int somar(int a, int b){
        return a+b;
    }

    public double somar(ArrayList<Integer> numeros){
        int somaLista = 0;
        for (Integer numero: numeros) {
            somaLista += numero;
        }
        return somaLista;
    }

    public int subtrair(int a, int b){
        return a-b;
    }

    public int subtrair(ArrayList<Integer> numeros) {
        int menosLista = 0;
        Collections.sort(numeros, (o1, o2) -> o2.compareTo(o1));
        for (int i = 0; i < numeros.size(); i++ ) {
            menosLista += numeros.get(i) - numeros.get(i++);
        }
        return menosLista;
    }

    public int multiplicar(int a, int b) {
        return a*b;
    }

    public ArrayList<Integer> multiplicar(ArrayList<Integer> numeros, int multiplicador) {
        ArrayList<Integer> numerosNovos = new ArrayList<>();
        for (Integer numero: numeros) {
            numero *= multiplicador;
            numerosNovos.add(numero);
        }
        return numerosNovos;
    }

    public double dividir(int a, int b){
        return a/b;
    }

    public double dividir(ArrayList<Integer> numeros) {
        int somaValoresPares = 0;
        int somaValoresImpares = 0;

        for (Integer numero: numeros) {
            if (numero % 2 == 0) {
                somaValoresPares += numero;
            } else {
                somaValoresImpares += numero;
            }
        }
        return somaValoresPares/somaValoresImpares;
    }
}