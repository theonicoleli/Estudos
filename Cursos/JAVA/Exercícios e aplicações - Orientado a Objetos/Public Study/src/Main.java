public class Main{
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria();
        conta.numeroContaRandom();
        do {
            conta.menuInicial();
        }while(true);
    }
}