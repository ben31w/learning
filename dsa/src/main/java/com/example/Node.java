package com.example;

/**
 * LinkedList node
 * @param <T> generic type
 */
public class Node<T> {
    T val;
    Node<T> next;

    public Node(T data) {
        val = data;
        next = null;
    }
}