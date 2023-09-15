package application;

import entities.Carro;
import entities.Moto;
import entities.Veiculo;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Veiculo> veiculos = new ArrayList<>();
        Veiculo veiculoA = new Veiculo();
        Veiculo carroA = new Carro();
        Veiculo motoA = new Moto();

        veiculos.add(veiculoA);
        veiculos.add(carroA);
        veiculos.add(motoA);

        for (Veiculo veiculo: veiculos) {
            veiculo.acelerar();
        }
    }
}
