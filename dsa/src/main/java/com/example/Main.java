package com.example;

public class Main {
    public static void main(String[] args) {
        MyArrayList<Character> arrList = new MyArrayList<>();
        arrList.append('A');
        arrList.append('E');
        arrList.insert('C', 1);
        System.out.println(arrList);

        MySinglyLinkedList<Character>  linkedList = new MySinglyLinkedList<>();
        linkedList.append('B');
        linkedList.append('N');
        linkedList.append('W');
        linkedList.remove(1);
        linkedList.insert('M', 1);
        System.out.println(linkedList);

        MyHashTable ht = new MyHashTable();
        ht.put("ben", 'b');
        System.out.println(ht.get("ben"));
    }
}
