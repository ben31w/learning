package com.example;

class Node<Character> {
    private char val;
    private Node<Character> next;

    public Node(char c) {
        val = c;
        next = null;
    }

    public char getVal() {
        return val;
    }

    public Node<Character> getNext() {
        return next;
    }

    public void setVal(char c) {
        val = c;
    }

    public void setNext(Node<Character> node) {
        next = node;
    }

    public void clearNext() {
        next = null;
    }
}


public class MyLinkedList<Character> implements MyList<Character>{
    private Node<Character> head;
    private Node<Character> tail;
    private int size;

    public MyLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }

//    /**
//     * Initialize an ArrayList from an existing array.
//     * @param existing
//     */
//    public MyLinkedList(char[] existing) {
//        if (existing.length == 0) {
//            head = null;
//            size = 0;
//        } else {
//            head = new Node<Character>(existing[0]);
//            size = existing.length;
//            for (int i = 0; i < existing.length; i++) {
//
//            }
//        }
//    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node<Character> curr = head;
        for (int i = 0; i < size; i++) {
            sb.append(curr.getVal());
            curr = curr.getNext();
        }
        return sb.toString();
    }

    /**
     * Return size of list. O(1)
     * @return size
     */
    @Override
    public int getSize() {
        return size;
    }

    /**
     * Get item at given index. O(N)
     * @param index  index indicating item to get
     * @return item or IndexOutOfBoundsException
     */
    @Override
    public char get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("index must be between [0, " + size + ")");
        }

        Node<Character> n = head;
        for (int i = 0; i < index; i++) {
            n = n.getNext();
        }
        return n.getVal();
    }

    /**
     * Remove (and return) item at given index. O(N)
     *
     * @param index index indicating item to get
     * @return item removed at index
     */
    @Override
    public char remove(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("index must be between [0, " + size + ")");
        } else if (index == 0 && size == 1) {
            char result = head.getVal();
            head = null;
            tail = null;

            --size;
            return result;
        } else {
            Node<Character> prev = head;
            Node<Character> curr = head.getNext();
            for (int i = 1; i < index; i++) {
                prev = curr;
                curr = curr.getNext();
            }

            char result = curr.getVal();
            prev.setNext(curr.getNext());

            --size;
            return result;
        }
    }

    /**
     * Append/add item to end of list. O(1)
     *
     * @param valueToAppend item to add to end of list
     */
    @Override
    public void append(char valueToAppend) {
        if (size == 0) {
            head = new Node<>(valueToAppend);
            tail = head;
        } else {
            tail.setNext(new Node<>(valueToAppend));
            tail = tail.getNext();
        }
        ++size;
    }

    /**
     * Insert item at given index. O(_)
     *
     * @param valueToInsert item to insert into list
     * @param index         index indicating where to insert
     */
    @Override
    public void insert(char valueToInsert, int index) {

    }
}
