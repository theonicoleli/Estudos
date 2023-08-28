import java.util.*;

public class Main {
    public static void main(String[] args) {


        //Dicionário em Java
        System.out.println("HASHTABLE");
        Hashtable<String, Integer> hashtable = new Hashtable<>() {{
            put("Théo", 19);
            put("Vini", 23);
            put("José", 32);
        }};
        hashtable.remove("José");
        int sizeHashTable = hashtable.size();
        System.out.println("O tamanho do hashtable é de: " + sizeHashTable);
        for (String key : hashtable.keySet()) {
            Integer value = hashtable.get(key);
            System.out.printf("O dicionário é: %s\nE seu valor é: %d", key, value);
            System.out.println();
        }

        System.out.println();

        //Conjuntos em Java
        System.out.println("HASHSET");
        HashSet<Integer> hashset = new HashSet<>() {{
            add(19); // Para adicionar elementos em Conjuntos assim como lista se faz com add
            add(23);
            add(72);
            add(23); // Conjuntos não repetem valores
        }};
        hashset.remove(19); // removendo um valor em conjunto
        int sizeHashSet = hashset.size();
        System.out.println("O tamanho do hashset é de: " + sizeHashSet);
        for (Integer i : hashset) {
            System.out.println(i);
        }

        System.out.println();

        // Assim como o HashTable ele funciona como um dicionário;
        // A principal diferença é que o HashMap pode armazenar valores nulos;
        // HashMap é mais rápido que HashTable;
        // É mais eficiente para iterar e possui melhor desempenho em geral.
        System.out.println("HASHMAP");
        HashMap<String, Integer> hashmap = new HashMap() {{
            put("Théo", 19);
            put("Vini", 23);
            put("Rogério", 51);
            put("Messi", 36);
        }};
        for (String key : hashmap.keySet()) {
            Integer values = hashmap.get(key);
            System.out.printf("O dicionário é %s\nSeu valor é %d", key, values);
            System.out.println();
        }
        // Ou poderia ser feito assim:
        for (Map.Entry<String, Integer> entry : hashmap.entrySet()) {
            String key = entry.getKey();
            Integer values = entry.getValue();
            System.out.printf("O dicionário é %s\nSeu valor é %d", key, values);
            System.out.println();
        }


        System.out.println();
        // Iterator é utilizado quando você quer verificar o próximo elemento
        // Ou anterior, remover o elemento, verificar se tem próximo elemento

        System.out.println("ITERATOR");
        ArrayList<Integer> arraylist = new ArrayList() {{
            add(19);
            add(23);
            add(72);
            add(43);
        }};

        Iterator<Integer> iterator = arraylist.iterator();
        while(iterator.hasNext()) {
            Integer value = iterator.next();
            System.out.println("Número: " + value);
        }
    }
}