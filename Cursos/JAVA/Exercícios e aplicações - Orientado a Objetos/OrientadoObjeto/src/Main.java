import java.util.Scanner;
import java.lang.reflect.Field;

public class Main {
    public static void main(String[] args) {
        do {
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

                String[] moedas = {"10", "50", "25", "100"};
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
                if (menu(quantidadeRefri, refri, armazenamento)) {
                    break;
                }

            } catch (Exception e) {
                System.out.println("Ocorreu um erro: " + e.getMessage());
            }
        } while (true);
    }
    public static boolean menu(int quantidadeRefri, Refri[] refri, Moedeiro moedeiro) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            for (int i = 0; i < quantidadeRefri; i++) {
                System.out.println("[" + (i+1) + "] " + refri[i].nome + " - " + refri[i].preco + "R$");
            }
            System.out.println("[S]air");
            System.out.println("Digite ao lado qual refri você deseja: ");

            try {
                String refriEscolhido = scanner.nextLine();
                if (!refriEscolhido.equalsIgnoreCase("S")) {
                    int refriIndex = Integer.parseInt(refriEscolhido) - 1;
                    if (refriIndex == 36) menuAdm(quantidadeRefri, refri, moedeiro);
                    System.out.println();
                    pagamento(refriIndex, refri, moedeiro);
                } else {
                    return true;
                }
            } catch (Exception e) {
                System.out.println("Opção inválida. Tente novamente.");
            }
        }
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
            if (troco == 0) refri[refriEscolhido].quantidade -= 1;
            else calcularTroco(troco, moedeiro); refri[refriEscolhido].quantidade -= 1;
        } else {
            System.out.println("Pagamento insuficiente.");
        }
    }

    public static void calcularTroco(double troco, Moedeiro armazenamento) {
        int[] moedasValores = {100, 50, 25, 10};
        int[] cedulasValores = {1000, 500, 200};

        int trocoEmCentavos = (int) (troco * 100);

        for (int moeda : moedasValores) {
            int quantidadeMoedas = trocoEmCentavos / moeda;
            try {
                Field moedaField = armazenamento.getClass().getDeclaredField("moedas_" + moeda);
                int moedaQuantidade = moedaField.getInt(armazenamento);

                if (quantidadeMoedas > 0 && quantidadeMoedas <= moedaQuantidade) {
                    trocoEmCentavos -= quantidadeMoedas * moeda;
                    moedaField.setInt(armazenamento, moedaQuantidade - quantidadeMoedas);
                    System.out.println("Troco: " + quantidadeMoedas + " moeda(s) de " + moeda / 100.0 + "R$");
                }
            } catch (Exception e) {
                System.out.println("Erro ao acessar moeda: " + e.getMessage());
            }
        }

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

        if (trocoEmCentavos == 0) {
            System.out.println("Troco fornecido corretamente.");
        } else {
            System.out.println("Não é possível fornecer troco exato com as moedas e cédulas disponíveis.");
        }
    }

    public static void menuAdm(int quantidadeRefri, Refri[] refri, Moedeiro moedeiro) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("-=-=-= Bem Vindo, adm =-=-=-");
        for (int i = 0; i < quantidadeRefri; i++) {
            System.out.println("[" + (i+1) + "]" + " A quantidade de " + refri[i].nome + " é de: " + refri[i].quantidade);
        }
        System.out.println("Digite o número do refri ao qual deseja acrescentar (0 para ir ao outro menu): ");
        try {
            int selecaoAdm = scanner.nextInt();
            switch (selecaoAdm) {
                case 0:
                    System.out.println("A quantidade de moedas disponíveis são de: ");
                    String[] moedas = {"10", "50", "25", "100"};
                    String[] cedulas = {"2", "5", "10"};

                    for (String moeda : moedas) {
                        try {
                            Field moedaField = moedeiro.getClass().getDeclaredField("moedas_" + moeda);
                            moedaField.setAccessible(true);
                            int moedaQuantidade = moedaField.getInt(moedeiro);
                            System.out.println("A quantidade de moedas de " + moeda + " é de: " + moedaQuantidade);
                        } catch (Exception e) {
                            System.out.println("Erro ao acessar moeda: " + e.getMessage());
                        }
                    }
                    for (String cedula : cedulas) {
                        try {
                            Field cedulaField = moedeiro.getClass().getDeclaredField("cedula_" + cedula);
                            cedulaField.setAccessible(true);
                            int cedulaQuantidade = cedulaField.getInt(moedeiro);
                            System.out.println("A quantidade de cedulas de " + cedula + " é de: " + cedulaQuantidade);
                        } catch (Exception e) {
                            System.out.println("Erro ao acessar moeda: " + e.getMessage());
                        }
                    }
                    break;
                default:
                    System.out.println("Digite a quantidade a ser acrescentada: ");
                    if (scanner.hasNextInt()) {
                        int quantidadeAdicionada = scanner.nextInt();
                        refri[selecaoAdm - 1].quantidade += quantidadeAdicionada;
                        System.out.println("A nova quantidade de " + refri[selecaoAdm - 1].nome + " é de: " + refri[selecaoAdm - 1].quantidade);
                    } else {
                        System.out.println("Digite algo válido.");
                    }
                    break;
            }
        } catch (Exception e) {
            System.out.println("Digite algo válido!");
        }
    }
}