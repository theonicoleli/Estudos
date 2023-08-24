import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Empresa> listEmpresa = new ArrayList<>();
        ArrayList<Carros> list = new ArrayList<>();
        Scanner sc = new Scanner(System.in);

        System.out.println("LISTA DE EMPRESA DE CARROS: ");

        System.out.print("Digite a quantidade de empresas: ");
        int quantidadeEmpresas = sc.nextInt();

        for (int i = 0; i < quantidadeEmpresas; i++) {

            System.out.print("\nDigite o nome da empresa: ");
            String empresa = sc.nextLine();
            sc.nextLine();

            System.out.print("Digite a quantidade de novos carros: ");

            int quantidadeCarros = sc.nextInt();
            for (int j = 0; j < quantidadeCarros; j++) {
                System.out.print("Digite o número da id: ");
                int id = sc.nextInt();
                System.out.print("Escreva o modelo do carro: ");
                String modelo = sc.next();
                System.out.print("Qual é a cor? ");
                String cor = sc.next();
                sc.nextLine();
                System.out.print("Digite o ano do carro: ");
                int ano = sc.nextInt();
                System.out.print("Digite o valor do carro: ");
                double valor = sc.nextDouble();

                list.add(new Carros(id, modelo, cor, ano, valor));
            }

            System.out.print("Digite o número da ID que você deseja alterar o valor: ");
            int id = sc.nextInt();
            for (Carros carros: list) {
                if (carros.getId() == id) {
                    System.out.printf("O valor do carro é: %.2f\n", carros.getValor());
                    System.out.print("Digite o novo valor do carro: ");
                    double newValor = sc.nextDouble();
                    carros.setNewValor(newValor);
                    System.out.printf("O novo valor do carro é: %.2f", carros.getValor());
                }
            }

            listEmpresa.add(new Empresa(empresa, list));
        }

        for (Empresa empresa : listEmpresa) {
            System.out.println(empresa.getNome());
            empresa.getAllCars();
        }
    }
}