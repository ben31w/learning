package com.example;

class Node<T> {
    T val;
    Node<T> next;

    public Node(T data) {
        val = data;
        next = null;
    }
}


/**
 * Singly-linked list implementation.
 * Linked Lists are usually doubly-linked.
 *
 * Singly-linked lists are optimized for appending/adding to the end: O(1).
 */
public class MySinglyLinkedList<T> implements MyList<T> {
    private Node<T> head;
    private Node<T> tail;
    private int size;

    public MySinglyLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }

   /**
    * Initialize an ArrayList from an existing array.
    * @param existing
    */
   public MySinglyLinkedList(T[] existing) {
       if (existing.length == 0) {
           head = null;
           tail = null;
           size = 0;
       } else {
           head = new Node<>(existing[0]);
           size = existing.length;

           Node<T> n = head;
           for (int i = 1; i < existing.length; i++) {
                n.next = new Node<>(existing[i]);
                n = n.next;
           }
           tail = n;
       }
   }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        Node<T> curr = head;
        for (int i = 0; i < size; i++) {
//            System.out.println(i + ": " + curr.val);
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
    public T get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("index must be between [0, " + size + ")");
        }

        Node<T> n = head;
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
    public T remove(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("index must be between [0, " + size + ")");
        } else if (index == 0) {
            T result = head.val;

            if (size == 1) {
                head = null;
                tail = null;
            } else {
                head = head.next;
            }

            --size;
            return result;
        } else {
            Node<T> prev = head;
            Node<T> curr = head.next;
            for (int i = 1; i < index; i++) {
                prev = curr;
                curr = curr.next;
            }

            T result = curr.val;
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
    public void append(T valueToAppend) {
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
    public void insert(T valueToInsert, int index) {
        if (index > size || index < 0) {
            throw new IndexOutOfBoundsException("index must be [0, " + size + ")");
        }

        if (index == size) {
            this.append(valueToInsert);
            return;
        }

        Node<T> n = head;
        for (int i = 0; i < index - 1; i++) {
            n = n.next;
        }

        Node<T> newNode = new Node<>(valueToInsert); // M
        if (n == tail) {
            newNode.next = tail;
        } else {
            newNode.next = n.next;  // M -> W
            n.next = newNode;  // B -> M
        }
        ++size;

        if (index == size - 1) {
            tail = newNode;
        } else if (index == 0) {
            head = newNode;
        }
    }
}
