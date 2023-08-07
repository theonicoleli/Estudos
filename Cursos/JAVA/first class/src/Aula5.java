import java.util.Date;
import java.util.Scanner;

public class Aula5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Date relogio = new Date();
        System.out.println("Horário exato de seu acesso: " + relogio);
        System.out.println("Deseja verificar oque:");
        System.out.println("\n1) Horas trabalhadas em decorrer dos anos:\n2) ");
        if (scanner.hasNextInt()) {
            int opcao = scanner.nextInt();
            if (opcao == 1) {
                verificarIntegridade();
            }
        } else {
            System.out.println("Digite algo válido!");
        }
    }
    public static void verificarIntegridade() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Você trabalha a quantos anos nesse departamento");
        if (scanner.hasNextInt()) {
            int anos = scanner.nextInt();
            System.out.println("Digite a quantidade de horas no dia: ");
            if (scanner.hasNextInt()) {
                int horas = scanner.nextInt();
                System.out.println("Calculando...");
                var workTime = (252 * anos) * horas;
                System.out.println("As horas trabalhadas durante todos esses anos foram: " + workTime);
            } else {
                System.out.println("Digite algo válido!");
            }
        } else {
            System.out.println("Digite algo válido!");
        }
    }
}
