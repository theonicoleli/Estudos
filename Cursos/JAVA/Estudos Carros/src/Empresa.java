import java.util.ArrayList;

public class Empresa {
    private String nome;
    public ArrayList<Carros> listCarros;

    public Empresa(String nome, ArrayList<Carros> listCarros) {
        this.nome = nome;
        this.listCarros = listCarros;
    }

    public void getAllCars() {
        for (Carros carros: listCarros) {
            carros.showCar();
        }
    }

    public String getNome() {
        return this.nome;
    }
}
