package com.example;

public class Main {
    public static void main(String[] args) {
        MyArrayList<Character> arrList = new MyArrayList<>();
        arrList.append('A');
        arrList.append('E');
        arrList.insert('C', 1);
        System.out.println(arrList);

        MyLinkedList<Character> linkedList = new MyLinkedList<>();
        linkedList.append('B');
        linkedList.append('N');
        linkedList.append('W');
        linkedList.remove(1);
        System.out.println(linkedList);
    }
}
