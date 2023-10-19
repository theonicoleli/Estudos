package entities;

public class Gerente extends Pessoa{
    private String setor;
    private Double salario;

    public Gerente(String nome, int idade, String peso, String setor, Double salario) {
        super(nome, idade, peso);
        this.setor = setor;
        this.salario = salario;
    }

    public String getSetor() {
        return setor;
    }

    public void setSetor(String setor) {
        this.setor = setor;
    }

    public Double getSalario() {
        return salario;
    }

    public void setSalario(Double salario) {
        this.salario = salario;
    }

    public void mostrarGerente() {
        System.out.println("Nome: " + getNome() + "\nIdade: " + getIdade() + "\nPeso: " + getPeso() + "\nSetor: " + this.setor + "\nSalário: " + this.salario);
    }
}
