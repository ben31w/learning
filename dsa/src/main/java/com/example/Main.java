package com.example;

public class Main {
    public static void main(String[] args) {
        MyArrayList<Character> charList = new MyArrayList<>();
        charList.append('A');
        charList.append('E');
        charList.insert('C', 1);
        System.out.println(charList);
    }
}
