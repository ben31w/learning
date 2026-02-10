package com.example;

public class MyArrayList<Character> implements MyList<Character> {
    /** Underlying array that stores the ordered elements. length = capacity. */
    private char[] arr;

    /** Actual size of list. */
    private int size;

    /**
     * Initialize an empty ArrayList with arbitrary capacity 10.
     */
    public MyArrayList() {
        size = 0;
        arr = new char[10];
    }

    /**
     * Initialize an ArrayList from an existing array. Double the
     * capacity of the array.
     * @param existing
     */
    public MyArrayList(char[] existing) {
        size = existing.length;

        arr = new char[existing.length * 2];
        for (int i = 0; i < existing.length; i++) {
            arr[i] = existing[i];
        }
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < size; i++) {
            sb.append(arr[i]);
        }
        return sb.toString();
    }

    /**
     * Return size of list. O(1)
     * @return size
     */
    public int getSize() {
        return size;
    }

    /**
     * Get item at given index. O(1)
     * @param index
     * @return item or IndexOutOfBoundsException
     */
    public char get(int index) {
        if (index < 0 || index >= size) {
            String msg = String.format("index must be between [0, %d)", size);
            throw new IndexOutOfBoundsException(msg);
        }
        return arr[index];
    }

    /**
     * Remove (and return) item at given index. O(N)
     * @param index
     * @return item removed at index
     */
    public char remove(int index) {
        if (index < 0 || index >= size) {
            String msg = String.format("index must be between [0, %d)", size);
            throw new IndexOutOfBoundsException(msg);
        }

        char result = arr[index];

        for (int i = index; i < size - 1; i++) {
            arr[i] = arr[i+1];
        }

        // The element at arr[size-1] isn't cleared, but because we
        // decrement the size of the list, it can't be accessed.
        --size;

        return result;
    }

    /**
     * Append/add item to end of list. 
     * Avg case: O(1)
     * Wors case: O(N)
     * @param valueToAppend
     */
    public void append(char valueToAppend) {
        if (arr.length == size) {
            char[] arrCopy = new char[arr.length * 2];
            for (int i = 0; i < size; i++) {
                arrCopy[i] = arr[i];
            }
            arr = arrCopy;
        }

        ++size;
        arr[size - 1] = valueToAppend;
    }

    /**
     * Insert item at given index. O(N)
     * @param valueToInsert
     * @param index
     */
    public void insert(char valueToInsert, int index) {
        if (index < 0 || index > size) {
            String msg = String.format("index must be between [0, %d]", size);
            throw new IndexOutOfBoundsException(msg);
        }

        if (arr.length == size) {
            char[] arrCopy = new char[arr.length * 2];

            // Up to index, simple copy item-for-item
            for (int i = 0; i < index; i++) {
                arrCopy[i] = arr[i];
            }

            arrCopy[index] = valueToInsert;
            
            // Past the index, insert items with an offset
            for (int i = index + 1 ; i < size + 1; i++) {
                arrCopy[i] = arr[i-1];
            }

            arr = arrCopy;
        }

        else {
            for (int i = size; i > index; i--) {
                arr[i] = arr[i-1];
            }

            arr[index] = valueToInsert;
        }

        ++size;
    }
}
