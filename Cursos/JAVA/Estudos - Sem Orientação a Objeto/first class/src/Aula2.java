import java.util.Scanner;

public class Aula2 {
    public static void main(String[] args) {
        while (true) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Digite a operação desejada: \n1) Multiplicação\n2) Divisão\n3) Soma\n4) Subtração\n5) Fatorial");
            int op = scanner.nextInt();
            int resultado = execucao(op);
            System.out.println("Resultado: " + resultado);
        }
    }
    public static int execucao(int op) {
        if (op >= 1 && op <= 4) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Digite o primeiro número: ");
            int num1 = scanner.nextInt();
            System.out.println("Digite o segundo número: ");
            int num2 = scanner.nextInt();
            if (op == 1) {
                return num1 * num2;
            } else if (op == 2) {
                return num1 / num2;
            } else if (op == 3) {
                return num1 + num2;
            } else if (op == 4) {
                return num1 - num2;
            }
        } else {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Digite um número para o fatorial");
            int num = scanner.nextInt();
            int fatorial = 1;
            for (int i = num; i > 0; i--) {
                fatorial = fatorial * i;
            }
            return fatorial;
        }
        return 0;
    }
}

