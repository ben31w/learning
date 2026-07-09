package com.example;

/**
 * TODO Not done yet
 * Doubly-Linked list node
 * @param <T>  generic type
 */
class DNode<T> {
    T val;
    DNode<T> prev;
    DNode<T> next;

    public DNode(T val) {
        this.val = val;
    }

    public DNode(T val, DNode<T> prev, DNode<T> next) {
        this.val = val;
        this.prev = prev;
        this.next = next;
    }
}

public class MyDoublyLinkedList<T> implements MyList<T> {
    private DNode<T> head;
    private DNode<T> tail;
    private int size;

    public MyDoublyLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }


    /**
     * Return size of list. O(_)
     *
     * @return size
     */
    @Override
    public int getSize() {
        return size;
    }

    /**
     * Get item at given index. O(_)
     *
     * @param index index indicating item to get
     * @return item or IndexOutOfBoundsException
     */
    @Override
    public T get(int index) {
        return null;
    }

    /**
     * Remove (and return) item at given index. O(_)
     *
     * @param index index indicating item to get
     * @return item removed at index
     */
    @Override
    public T remove(int index) {
        return null;
    }

    /**
     * Append/add item to end of list. O(_)
     *
     * @param valueToAppend item to add to end of list
     */
    @Override
    public void append(T valueToAppend) {

    }

    /**
     * Insert item at given index. O(_)
     *
     * @param valueToInsert item to insert into list
     * @param index         index indicating where to insert
     */
    @Override
    public void insert(T valueToInsert, int index) {

    }
}
