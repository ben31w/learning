package com.example;

/**
 * Very simple hash table implementation that supports
 * put(String key, char value) and get(String key).
 *
 * It's supposed to use an array of singly-linked lists for chaining
 * (collision management), but it's not working.
 */
public class MyHashTable {
    MySinglyLinkedList[] arr = new MySinglyLinkedList[100];

    public MyHashTable() {

    }

    public void put(String key, char val) {
        int idx = hashString(key);
        if (arr[idx] == null) {
            arr[idx] = new MySinglyLinkedList();
        }
        arr[idx].append(val);
    }

    public char get(String key) {
        int idx = hashString(key);
        MySinglyLinkedList ll = arr[idx];
        // TODO this won't work if there's a collision
        // there SinglyLinkedList needs to store K,V pairs, not just V
        return ll.get(0);
    }

    /**
     * Very simple hash function that takes string -> int[0-99].
     *
     * @param key  string to hash
     * @retrun hashed key, an int[0-99]
     */
    private int hashString(String key) {
        int sum = 0;
        // not worth summing all chars if the string is long. Cap at 5.
        int numChars = Math.min(5, key.length());

        for (int i = 0; i < numChars; i ++) {
            sum += key.charAt(i);
        }

        return sum % 100;
    }
}
