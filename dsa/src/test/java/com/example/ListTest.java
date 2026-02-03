package com.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ListTest {

    private char[] initialData = {'a', 'b', 'c', 'd'};
    private final MyArrayList<Character> charList = new MyArrayList<>(initialData);

    @Test
    void getSizeTest() {
        assertEquals(4, charList.getSize());
    }

    @Test
    void getTest() {
        assertEquals('a', charList.get(0));
        assertEquals('b', charList.get(1));
    }

    @Test
    void removeTest() {
        char item1 = charList.remove(1);
        assertEquals(
            'b', 
            item1,
            "charList should be \"acd\", actual: \"" + charList + "\""
        );
        assertEquals(3, charList.getSize());
    }

    @Test
    void removeOutOfBoundsTest() {
        assertThrows(
            IndexOutOfBoundsException.class,
            () -> charList.remove(10),
            "remove should throw IndexOutOfBoundsException"
        );
    }

    @Test
    void appendTest() {
        charList.append('e');
        assertEquals(
            'e', 
            charList.get(charList.getSize() - 1),
            "charList should be \"abcde\", actual: \"" + charList + "\""
        );
        assertEquals(
            5,
            charList.getSize()
        );
    }

    @Test
    void append2Test() {
        charList.append('e');
        charList.append('f');
        assertEquals('e', charList.get(charList.getSize() - 2));
        assertEquals('f', charList.get(charList.getSize() - 1));
        assertEquals(6, charList.getSize());
    }

    @Test
    void insertTest() {
        charList.insert('e', 2);
        assertEquals('e', charList.get(2));
        assertEquals(5, charList.getSize());
    }

    @Test
    void insertOutOfBoundsTest() {
        assertThrows(
            IndexOutOfBoundsException.class,
            () -> charList.insert('e', 10),
            "insert should throw IndexOutOfBoundsException"
        );
    }
}
