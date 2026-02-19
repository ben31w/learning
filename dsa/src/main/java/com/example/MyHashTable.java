package com.example;

import java.security.KeyException;

/**
 * Very simple hash table implementation that supports
 * put(String key, V value) and get(String key).
 * Uses an array of singly-linked lists for collision management.
 */
public class MyHashTable<V> {
    MySinglyLinkedList<Pair<String, V>>[] arr = new MySinglyLinkedList[100];

    public MyHashTable() {

    }

    public void put(String key, V val) {
        int idx = hashString(key);
        if (arr[idx] == null) {
            arr[idx] = new MySinglyLinkedList<>();
        }
        arr[idx].append(new Pair<>(key, val));
    }

    /**
     * O(1)
     * @param key  get value at this key
     * @return  value or null
     */
    public V get(String key) {
        int idx = hashString(key);
        MySinglyLinkedList<Pair<String, V>>  ll = arr[idx];

        if (ll == null) {
            return null;
        }

        for (int i = 0; i < ll.getSize(); i++) {
            Pair<String, V> pair = ll.get(i);
            if (pair.obj1.equals(key)) {
                return pair.obj2;
            }
        }

        return null;
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
