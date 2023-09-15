package application;

import entitie.enumerator.Color;
import entities.Circle;
import entities.Rectangle;
import entities.Shape;

import java.util.ArrayList;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Shape> shapes = new ArrayList<>();
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of shapes: ");
        int exec = sc.nextInt();

        for (int i = 1; i <= exec; i++) {
            System.out.println("Shape #" + i + " data:");
            System.out.print("Rectangle or Circle (r/c)? ");
            char ch = sc.next().charAt(0);

            System.out.print("Color (BLACK/BLUE/RED): ");
            Color color = Color.valueOf(sc.next());

            if (ch == 'r') {

                System.out.print("Width: ");
                double width = sc.nextDouble();
                System.out.print("Height: ");
                double height = sc.nextDouble();

                shapes.add(new Rectangle(color, width, height));
            } else if (ch == 'c') {

                System.out.print("Radius: ");
                double radius = sc.nextDouble();

                shapes.add(new Circle(color, radius));
            } else {
                System.out.println("Something wrong happened");
            }
        }

        System.out.println("SHAPE AREAS: ");
        for (Shape shape: shapes) {
            if (shape instanceof Circle) {
                System.out.println(shape.toString());
            } else if (shape instanceof Rectangle) {
                System.out.println(shape.toString());
            } else {
                return;
            }
        }

        sc.close();
    }
}