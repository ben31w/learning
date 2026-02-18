package com.example;

public class Pair<T, U> {
    T obj1;
    U obj2;

    public Pair(T obj1, U obj2) {
        this.obj1 = obj1;
        this.obj2 = obj2;
    }

    public String toString() {
        return "<" + obj1 + ", " + obj2 + ">";
    }
}
