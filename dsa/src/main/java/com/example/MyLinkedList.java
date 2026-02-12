package com.example;

class Node<Character> {
    char val;
    Node<Character> next;

    public Node(char c) {
        val = c;
        next = null;
    }
}


/**
 * Singly-linked list implementation
 */
public class MyLinkedList<Character> implements MyList<Character>{
    private Node<Character> head;
    private Node<Character> tail;
    private int size;

    public MyLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }

   /**
    * Initialize an ArrayList from an existing array.
    * @param existing
    */
   public MyLinkedList(char[] existing) {
       if (existing.length == 0) {
           head = null;
           tail = null;
           size = 0;
       } else {
           head = new Node<Character>(existing[0]);
           size = existing.length;

           Node<Character> n = head;
           for (int i = 1; i < existing.length; i++) {
                n.next = new Node<>(existing[i]);
                n = n.next;
           }
           tail = n;
       }
   }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node<Character> curr = head;
        for (int i = 0; i < size; i++) {
            sb.append(curr.val);
            curr = curr.next;
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
            n = n.next;
        }
        return n.val;
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
        } else if (index == 0) {
            char result = head.val;

            if (size == 1) {
                head = null;
                tail = null;
            } else {
                head = head.next;
            }

            --size;
            return result;
        } else {
            Node<Character> prev = head;
            Node<Character> curr = head.next;
            for (int i = 1; i < index; i++) {
                prev = curr;
                curr = curr.next;
            }

            char result = curr.val;
            prev.next = curr.next;

            if (index == size - 1) {
                tail = prev;
            }

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
            tail.next = new Node<>(valueToAppend);
            tail = tail.next;
        }
        ++size;
    }

    /**
     * Insert item at given index. O(N)
     *
     * @param valueToInsert item to insert into list
     * @param index         index indicating where to insert
     */
    @Override
    public void insert(char valueToInsert, int index) {
        if (index >= size || index < 0) {
            throw new IndexOutOfBoundsException("index must be [0, " + size + ")");
        }

        Node<Character> n = head;
        for (int i = 0; i < index; i++) {
            n = n.next;
        }

        Node<Character> newNode = new Node<>(valueToInsert);
        newNode.next =  n.next;
        n.next = newNode;
        ++size;

        if (index == size - 1) {
            tail = newNode;
        } else if (index == 0) {
            head = newNode;
        }
    }
}
