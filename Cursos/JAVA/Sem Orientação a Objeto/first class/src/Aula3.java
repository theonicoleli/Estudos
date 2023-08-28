import java.util.Scanner;

public class Aula3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite seu nome: ");
        String nome = scanner.nextLine();
        char[] caracteres = nome.toCharArray();
        for (int i = 0; i < caracteres.length / 2; i++) {
            char temp = caracteres[i];
            caracteres[i] = caracteres[caracteres.length - 1 -i];
            caracteres[caracteres.length - 1 -i] = temp;
        }
        for (var letra : caracteres) {
            System.out.println(letra);
        }
        String newfrase = new String(caracteres);
        System.out.println("Seu nome invertido é: " + newfrase);
    }
}
