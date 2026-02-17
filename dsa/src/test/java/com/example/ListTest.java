package com.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ListTest {

    private final char[] initialData = {'a', 'b', 'c', 'd'};
    private final MyArrayList<Character> al = new MyArrayList<>(initialData);
    private final MySinglyLinkedList<Character> ll = new MySinglyLinkedList<>(initialData);

    @Test
    void getSizeArrayListTest() {
        assertEquals(4, al.getSize());
    }

    @Test
    void getArrayListTest() {
        assertEquals('a', al.get(0));
        assertEquals('b', al.get(1));
    }

    @Test
    void removeArrayListTest() {
        char item1 = al.remove(1);
        assertEquals(
                'b',
                item1,
                "al should be \"acd\", actual: \"" + al + "\""
        );
        assertEquals(3, al.getSize());
    }

    @Test
    void removeOutOfBoundsArrayListTest() {
        assertThrows(
                IndexOutOfBoundsException.class,
                () -> al.remove(10),
                "remove should throw IndexOutOfBoundsException"
        );
    }

    @Test
    void appendArrayListTest() {
        al.append('e');
        assertEquals(
                'e',
                al.get(al.getSize() - 1),
                "al should be \"abcde\", actual: \"" + al + "\""
        );
        assertEquals(
                5,
                al.getSize()
        );
    }

    @Test
    void append2ArrayListTest() {
        al.append('e');
        al.append('f');
        assertEquals('e', al.get(al.getSize() - 2));
        assertEquals('f', al.get(al.getSize() - 1));
        assertEquals(6, al.getSize());
    }

    @Test
    void insertArrayListTest() {
        al.insert('e', 2);
        assertEquals('e', al.get(2));
        assertEquals(5, al.getSize());
    }

    @Test
    void insertOutOfBoundsArrayListTest() {
        assertThrows(
                IndexOutOfBoundsException.class,
                () -> al.insert('e', 10),
                "insert should throw IndexOutOfBoundsException"
        );
    }

    @Test
    void getSizeLinkedListTest() {
        assertEquals(4, ll.getSize());
    }

    @Test
    void getLinkedListTest() {
        assertEquals('a', ll.get(0));
        assertEquals('b', ll.get(1));
    }

    @Test
    void removeLinkedListTest() {
        char item1 = ll.remove(1);
        assertEquals(
                'b',
                item1,
                "ll should be \"acd\", actull: \"" + ll + "\""
        );
        assertEquals(3, ll.getSize());
    }

    @Test
    void removeOutOfBoundsLinkedListTest() {
        assertThrows(
                IndexOutOfBoundsException.class,
                () -> ll.remove(10),
                "remove should throw IndexOutOfBoundsException"
        );
    }

    @Test
    void appendLinkedListTest() {
        ll.append('e');
        assertEquals(
                'e',
                ll.get(ll.getSize() - 1),
                "ll should be \"abcde\", actull: \"" + ll + "\""
        );
        assertEquals(
                5,
                ll.getSize()
        );
    }

    @Test
    void append2LinkedListTest() {
        ll.append('e');
        ll.append('f');
        assertEquals('e', ll.get(ll.getSize() - 2));
        assertEquals('f', ll.get(ll.getSize() - 1));
        assertEquals(6, ll.getSize());
    }

    @Test
    void insertLinkedListTest() {
        ll.insert('e', 2);
        assertEquals('e', ll.get(2));
        assertEquals(5, ll.getSize());
    }

    @Test
    void insertOutOfBoundsLinkedListTest() {
        assertThrows(
                IndexOutOfBoundsException.class,
                () -> ll.insert('e', 10),
                "insert should throw IndexOutOfBoundsException"
        );
    }
}
