package com.example;

public interface MyList {
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
    char get(int index);

    /**
     * Remove (and return) item at given index. O(_)
     * @param index  index indicating item to get
     * @return item removed at index
     */
    char remove(int index);

    /**
     * Append/add item to end of list. O(_)
     * @param valueToAppend  item to add to end of list
     */
    void append(char valueToAppend);

    /**
     * Insert item at given index. O(_)
     * @param valueToInsert  item to insert into list
     * @param index  index indicating where to insert
     */
    void insert(char valueToInsert, int index);
}