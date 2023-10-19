import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<ArrayList> matriz = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite o número de linhas: ");
        int qLinhas = sc.nextInt();
        System.out.print("Digite o número de colunas: ");
        int qColunas = sc.nextInt();
        for (int i = 0; i < qLinhas; i++) {
            ArrayList<Integer> row = new ArrayList<>();
            for (int j = 0; j < qColunas; j++) {
                System.out.print("Digite o valor para a posição (" + i + ", " + j + "): ");
                row.add(sc.nextInt());
            }
            matriz.add(row);
        }
        matriz.forEach(linha -> System.out.println(linha));
        sc.close();
    }
}