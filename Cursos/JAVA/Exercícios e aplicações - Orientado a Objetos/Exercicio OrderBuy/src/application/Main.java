package application;

import entities.Client;
import entities.Order;
import entities.OrderItem;
import entities.Product;
import entitiesEnum.OrderStatus;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.Instant;
import java.util.Date;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws ParseException {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter cliente data: ");
        System.out.print("Name: ");
        String name = sc.nextLine();
        System.out.print("Email: ");
        String email = sc.nextLine();
        System.out.print("Birth date (DD/MM/YYYY): ");
        String inputDate = sc.nextLine();
        SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
        Date date = dateFormat.parse(inputDate);

        Client client = new Client(name, email, date);

        System.out.println("Enter order data: ");
        System.out.print("Status: ");
        OrderStatus orderStatus = OrderStatus.valueOf(sc.nextLine());

        OrderItem orderItem = new OrderItem();
        System.out.println("How many items to this order: ");
        int amountTimes = sc.nextInt();

        for (int i = 1; i <= amountTimes; i++ ) {
            System.out.printf("Enter #%d item data: \n", i);
            sc.nextLine();
            System.out.print("Product name: ");
            String productName = sc.nextLine();
            System.out.print("Product price: ");
            double price = sc.nextDouble();
            System.out.print("Quantity: ");
            int quantity = sc.nextInt();

            Product product = new Product(productName, price);
            orderItem.addProduct(product, quantity);
        }

        Instant now = Instant.now();
        Date dateOrder = new Date(now.toEpochMilli());
        Order order = new Order(dateOrder, orderStatus);

        System.out.println("Order summary: ");
        System.out.println("Order moment: " + order.getStatus());
        System.out.println("Client: " + client.getClient());
        System.out.println("Order items: ");
        orderItem.productsInformation();

        sc.close();
    }
}