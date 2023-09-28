package application;

import entities.Monaco;
import entities.Spa;

public class Program {
    public static void main(String[] args) {
        Monaco monaco = new Monaco();
        Spa spa = new Spa();
        System.out.println(monaco.infoPista());
        System.out.println(monaco.melhorTempo());

        System.out.println();

        System.out.println(spa.infoPista());
        System.out.println(spa.melhorTempo());

    }
}
