import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();

        list.add("Théo");
        list.add("Anthony");
        list.add("Ana");
        list.add("José");
        list.add(2, "Augusto");

        System.out.println();

        System.out.printf("O tamanho de sua lista é %d\n", list.size());
        list.forEach(nome -> System.out.println(nome));

        System.out.println();

        list.removeIf(x -> x.charAt(0) == 'T');
        list.forEach(nome -> System.out.println(nome));

        System.out.println();

        for (String nome: list) {
            System.out.printf("O index de %s é: %d\n", nome, list.indexOf(nome));
        }

        List<String> result = list.stream().filter(x -> x.charAt(0) == 'A').collect(Collectors.toList());
        result.forEach(nome -> System.out.println(nome));

        System.out.println();

        String name = list.stream().filter(x -> x.charAt(0) == 'J').findFirst().orElse(null);
        System.out.println(name);
    }
}