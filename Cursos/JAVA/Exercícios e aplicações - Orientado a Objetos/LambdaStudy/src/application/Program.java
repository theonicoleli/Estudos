package application;

import entities.Product;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.stream.Collectors;

public class Program {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);
        List<Product> list = new ArrayList<>();

        list.add(new Product("TV", 900.00));
        list.add(new Product("Mouse", 50.00));
        list.add(new Product("Tablet", 350.00));
        list.add(new Product("HD CASE", 80.90));

        /*double factor = 1.1;

        Consumer<Product> cons = p -> {
            p.setPrice(p.getPrice() * factor);
        };

        list.forEach(Product::nonStaticPriceUpdate);

        list.forEach(System.out::println);*/

        List<String> names =
                list.stream().map(Product::staticUpperCaseName).collect(Collectors.toList());

        names.forEach(System.out::println);
    }
}