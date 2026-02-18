package com.example;

public interface MyList<T> {
    /**
     * Return size of list. O(_)
     * @return size
     */
    int getSize();

    /**
     * Get item at given index. O(_)
     * @param index  index indicating item to get
     * @return item or IndexOutOfBoundsException
     */
    T get(int index);

    /**
     * Remove (and return) item at given index. O(_)
     * @param index  index indicating item to get
     * @return item removed at index
     */
    T remove(int index);

    /**
     * Append/add item to end of list. O(_)
     * @param valueToAppend  item to add to end of list
     */
    void append(T valueToAppend);

    /**
     * Insert item at given index. O(_)
     * @param valueToInsert  item to insert into list
     * @param index  index indicating where to insert
     */
    void insert(T valueToInsert, int index);
}