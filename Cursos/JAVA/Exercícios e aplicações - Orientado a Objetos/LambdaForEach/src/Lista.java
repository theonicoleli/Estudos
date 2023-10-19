import java.util.ArrayList;

public class Lista {
    private int lenLista;
    private ArrayList<Integer> lista = new ArrayList<Integer>();

    public ArrayList<Integer> criarLista(int ...a) {
        for (int num : a) {
            lista.add(num);
        }
        return lista;
    }

    public ArrayList<Integer> pegarLista() {
        return this.lista;
    }

    public void retornarLista(ArrayList lista) {
        System.out.println("A lista possui os valores: ");
        lista.forEach(num -> System.out.println("Número: " + num));
    }

    public void setLenLista(int tamanhoLista) {
        this.lenLista = tamanhoLista;
    }

    public int getLenLista() {
        return this.lenLista;
    }
}
