import java.util.Scanner;
import java.lang.reflect.Field;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite a quantidade de refri que você deseja adicionar à máquina: ");
        try {
            int quantidadeRefri = scanner.nextInt();
            Refri[] refri = new Refri[quantidadeRefri];

            for (int i = 0; i < quantidadeRefri; i++) {
                refri[i] = new Refri();
                System.out.println("Digite o preço do refri " + (i + 1) + ": ");
                refri[i].preco = scanner.nextDouble();
                scanner.nextLine();
                System.out.println("Digite o nome do refri " + (i + 1) + ": ");
                refri[i].nome = scanner.nextLine();
                System.out.println("Digite a quantidade do refri " + (i + 1) + ": ");
                refri[i].quantidade = scanner.nextInt();
            }

            Moedeiro armazenamento = new Moedeiro();

            String[] moedas = {"1", "50", "25", "10"};
            String[] cedulas = {"2", "5", "10"};

            for (String moeda : moedas) {
                System.out.println("Digite a quantidade de moedas de " + moeda + ": ");
                int quantidade = scanner.nextInt();
                Field moedaField = armazenamento.getClass().getDeclaredField("moedas_" + moeda);
                moedaField.setInt(armazenamento, quantidade);
            }

            for (String cedula : cedulas) {
                System.out.println("Digite a quantidade de cédulas de " + cedula + ": ");
                int quantidade = scanner.nextInt();
                Field cedulaField = armazenamento.getClass().getDeclaredField("cedula_" + cedula);
                cedulaField.setInt(armazenamento, quantidade);
            }

            menu(quantidadeRefri, refri, armazenamento);

        } catch (Exception e) {
            System.out.println("Ocorreu um erro: " + e.getMessage());
        }
    }
    public static void menu(int quantidadeRefri, Refri[] refri, Moedeiro moedeiro){
        for (int i = 0; i < quantidadeRefri; i++) {
            System.out.println("[" + (i+1) + "] " + refri[i].nome + " - " + refri[i].preco + "R$");
        }
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite ao lado qual refri você deseja: ");
        int refriEscolhido = scanner.nextInt();
        System.out.println();
        pagamento(refriEscolhido, refri, moedeiro);
    }

    public static void pagamento(int refriEscolhido, Refri[] refri, Moedeiro moedeiro) {
        double precoRefri = refri[refriEscolhido].preco;
        System.out.println("Seu pagamento será de: " + precoRefri + "R$");

        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o valor a ser inserido: ");
        double pagamento = scanner.nextDouble();

        if (pagamento >= precoRefri) {
            double troco = pagamento - precoRefri;
            System.out.println("Troco: " + troco + "R$");

            calcularTroco(troco, moedeiro);
        } else {
            System.out.println("Pagamento insuficiente.");
        }
    }

    public static void calcularTroco(double troco, Moedeiro armazenamento) {
        int[] moedasValores = {10, 25, 50, 100};
        int[] cedulasValores = {200, 500, 1000};

        int trocoEmCentavos = (int) (troco * 100);

        for (int cedula : cedulasValores) {
            int quantidadeCedulas = trocoEmCentavos / cedula;
            try {
                Field cedulaField = armazenamento.getClass().getDeclaredField("cedula_" + cedula / 100);
                int cedulaQuantidade = cedulaField.getInt(armazenamento);

                if (quantidadeCedulas > 0 && quantidadeCedulas <= cedulaQuantidade) {
                    trocoEmCentavos -= quantidadeCedulas * cedula;
                    cedulaField.setInt(armazenamento, cedulaQuantidade - quantidadeCedulas);
                    System.out.println("Troco: " + quantidadeCedulas + " cédula(s) de " + cedula / 100.0 + "R$");
                }
            } catch (Exception e) {
                System.out.println("Erro ao acessar cédula: " + e.getMessage());
            }
        }
    }
}