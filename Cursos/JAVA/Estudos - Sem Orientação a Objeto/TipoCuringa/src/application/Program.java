package application;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Program {
    public static void main(String[] args) {

        // No caso a baixo o get funciona corretamente, porém o put da erro de compilação.

        /*
        List<Integer> intList = new ArrayList<>();
        intList.add(10);
        intList.add(5);

        List<? extends Number> list = intList;

        Number x = list.get(0);

        list.add(20); // Erro compilação
        */

        // No caso a baixo o get gera um erro de compilação, porém o put funciona corretamente.

        /*
        List<Object> myObject = new ArrayList<>();
        myObject.add("Maria");
        myObject.add("Alex");

        List<? super Number> myNums = myObject;

        myNums.add(10);
        myNums.add(3.14);

        Number x = myNums.get(0); // Erro compilação
        */

        List<Integer> myInts = Arrays.asList(1, 2, 3, 4);
        List<Double> myDoubles = Arrays.asList(3.14, 6.28);
        List<Object> myObjs = new ArrayList<>();

        copy(myInts, myObjs);
        printList(myObjs);

        copy(myDoubles, myObjs);
        printList(myObjs);
    }

    public static void copy(List<? extends Number> source, List<? super Number> destiny) {
        for (Number number: source) {
            destiny.add(number);
        }
    }

    public static void printList(List<?> list) {
        for (Object obj : list) {
            System.out.println(obj + " ");
        }
        System.out.println();
    }
}