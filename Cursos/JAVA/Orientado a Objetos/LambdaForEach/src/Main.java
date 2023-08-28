import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Lista lista = new Lista();
        System.out.println("Seja bem vindo a sua mais nova lista!");
        System.out.println("Digite o tamanho para a lista: ");
        lista.setLenLista(scanner.nextInt());
        int[] numeros = new int[lista.getLenLista()];
        for (int n = 0; n < lista.getLenLista(); n++) {
            System.out.println("Digite o número para adicionar: ");
            numeros[n] = scanner.nextInt();
        }
        lista.criarLista(numeros);
        lista.retornarLista(lista.pegarLista());
     }
}