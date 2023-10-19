package application;

import entities.Animal;
import entities.Cachorro;
import entities.Gato;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Animal> animais = new ArrayList<>();
        Animal animalA = new Animal();
        Animal cachorroA = new Cachorro();
        Animal gatoA = new Gato();

        animais.add(animalA);
        animais.add(cachorroA);
        animais.add(gatoA);

        for (Animal animal: animais) {
            animal.fazerBarulho();
        }
    }
}
