package com.example;

public interface MyList<Character> {
    public int getSize();
    public char get(int index);
    public char remove(int index);
    public void append(char c);
    public void insert(char c, int index);
}