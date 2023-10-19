package application;

import entities.Product;

import java.io.*;
import java.util.ArrayList;

public class Program {
    public static void main(String[] args) {

        String document = "c:\\temp\\products.txt";
        String newDocument = "c:\\temp\\newProductsList.txt";

        ArrayList<Product> products = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(document))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",");
                if (parts.length == 3) {
                    String productName = parts[0].trim();
                    double productPrice = Double.parseDouble(parts[1].trim());
                    Integer productQuantity = Integer.parseInt(parts[2].trim());

                    products.add(new Product(productName, productPrice, productQuantity));
                }
            }

            for (Product product : products) {
                System.out.println(product.toString());
            }

            try (BufferedWriter bw = new BufferedWriter(new FileWriter(newDocument))) {
                for (Product product : products) {
                    String productInfo = "Product: " + product.getName() + ", Price: " + product.getPrice();
                    bw.write(productInfo);
                    bw.newLine();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
