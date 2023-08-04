import java.util.ArrayList;
import java.util.Scanner;
import java.util.Random;

public class Aula1 {
    // FUNÇÃO USANDO ARRAY COMO LISTA (ARRAY SÃO AQUELE TAMANHO PARA SEMPRE)
    //public static int[] randomValluesArray(int size){
        //int[] values = new int[size];
        //Random random = new Random();
        //for (int i = 0; i <= values.length; i++) {
            //values[i] = random.nextInt(0, 999);
        //}
        //return values;
    //}

    // FUNÇÃO USANDO LISTA (LISTAS CONSEGUEM SER MUDADAS NO MEIO DO PROCESSO)
    public static ArrayList<Integer> randomValuesList(int size) {
        ArrayList<Integer> values = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            values.add(random.nextInt(0, 999));
        }
        return values;
    }

    public static void main(String[] args) {
        while (true) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Digite a quantidade de números para sua lista: ");
            int size = scanner.nextInt();

            for (var value : randomValuesList(size)) {
                if (value % 3 == 0) {
                    System.out.println(value + " - Este número é múltiplo de 3");
                } else if (value % 2 == 0) {
                    System.out.println(value + " - Este número é par");
                } else {
                    System.out.println(value + " - Este número é impar");
                }
            }
        }
    }
}