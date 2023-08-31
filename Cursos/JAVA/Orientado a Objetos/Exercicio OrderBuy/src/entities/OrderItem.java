package entities;

import java.util.ArrayList;
import java.util.HashMap;

public class OrderItem {
    private final HashMap<Product, Integer> quantity;
    private Double finalPrice;
    private final ArrayList<Product> products;

    public OrderItem() {
        quantity = new HashMap<>();
        products = new ArrayList<>();
        finalPrice = 0.0;
    }

    public void addProduct(Product product, int quantity) {
        products.add(product);
        if (!this.quantity.containsKey(product))
            this.quantity.put(product, quantity);
    }

    public double returnValueProducts(Product product) {
        int productQuantity = quantity.get(product);
        double productPrice = product.getPrice();
        return productPrice * productQuantity;
    }

    private Double setFinalPrice() {
        for(Product product : products) {
            int productQuantity = quantity.get(product);
            double productPrice = product.getPrice();
            finalPrice += productQuantity * productPrice;
        }
        return finalPrice;
    }

    public Double getFinalPrice() {
        return setFinalPrice();
    }

    public void productsInformation() {
        for (Product product: products) {
            System.out.println(product.getName() + ", $" + product.getPrice() +
                    ", Quantity: " + quantity.get(product) +
                    ", Subtotal: " + returnValueProducts(product));
        }
        System.out.println("Final price: " + getFinalPrice());
    }
}
