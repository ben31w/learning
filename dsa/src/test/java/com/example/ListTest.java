package com.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ListTest {
    private final MyArrayList<Character>  al = new MyArrayList<>();
    private final MySinglyLinkedList<Character>  sll = new MySinglyLinkedList<>();

    @Test
    void getSizeALTest() {
        assertEquals(0, al.getSize());
        al.append('a');
        assertEquals(1, al.getSize());
        al.append('b');
        assertEquals(2, al.getSize());
        al.append('c');
        assertEquals(3, al.getSize());
    }

    @Test
    void getALTest() {
        al.append('a');
        al.append('b');
        al.append('c');

        assertEquals('a', al.get(0));
        assertEquals('b', al.get(1));
        assertEquals('c', al.get(2));

        assertThrows(
                IndexOutOfBoundsException.class,
                () -> al.get(-1),
                "Negative index should throw exception"
        );

        assertThrows(
                IndexOutOfBoundsException.class,
                () -> al.get(4),
                "Index out of range should throw exception"
        );
    }

    @Test
    void removeALTest() {
        al.append('a');
        al.append('b');
        al.append('c');

        char item1 = al.remove(1);

        assertEquals(
                'b',
                item1,
                "al should be \"ac\", actual: \"" + al + "\""
        );
        assertEquals(2, al.getSize());

        char item0 = al.remove(0);

        assertEquals(
                'a',
                item0,
                "al should be \"c\", actual: \"" + al + "\""
        );
        assertEquals(1, al.getSize());
    }

    @Test
    void removeOutOfBoundsALTest() {
        assertThrows(
                IndexOutOfBoundsException.class,
                () -> al.remove(10),
                "remove should throw IndexOutOfBoundsException"
        );
        assertThrows(
                IndexOutOfBoundsException.class,
                () -> al.remove(-1),
                "remove should throw IndexOutOfBoundsException"
        );
    }

    @Test
    void appendALTest() {
        al.append('a');
        assertEquals(
                'a',
                al.get(al.getSize() - 1),
                "al should be \"a\", actual: \"" + al + "\""
        );
        assertEquals(1, al.getSize());
    }

    @Test
    void insertALTest() {
        al.insert('b', 0);
        assertEquals('b', al.get(0));
        assertEquals(1, al.getSize());

        al.insert('a', 0);
        assertEquals('a', al.get(0));
        assertEquals(2, al.getSize());

        al.insert('c', 2);
        assertEquals('c', al.get(2));
        assertEquals(3, al.getSize());

        assertEquals(3, al.getSize());

        assertThrows(
                IndexOutOfBoundsException.class,
                () -> al.insert('d', 10),
                "insert should throw exception"
        );

        assertThrows(
                IndexOutOfBoundsException.class,
                () -> al.insert('d', -1),
                "insert should throw exception"
        );
    }

    @Test
    void atCapacityAppendALTest() {
        MyArrayList<Character> atCap = new MyArrayList<>(1);

        atCap.append('a');
        assertEquals(1, atCap.getSize());
        assertEquals('a', atCap.get(0));

        atCap.append('b');
        assertEquals(2, atCap.getSize());
        assertEquals('b', atCap.get(1));

        atCap.append('c');
        assertEquals(3, atCap.getSize());
        assertEquals('c', atCap.get(2));

        atCap.append('d');
        assertEquals(4, atCap.getSize());
        assertEquals('d', atCap.get(3));
    }

    @Test
    void getSizeSLLTest() {
        assertEquals(0, sll.getSize());
        sll.append('a');
        assertEquals(1, sll.getSize());
        sll.append('b');
        assertEquals(2, sll.getSize());
        sll.append('c');
        assertEquals(3, sll.getSize());
    }

    @Test
    void getSLLTest() {
        sll.append('a');
        sll.append('b');
        sll.append('c');

        assertEquals('a', sll.get(0));
        assertEquals('b', sll.get(1));
        assertEquals('c', sll.get(2));

        assertThrows(
                IndexOutOfBoundsException.class,
                () -> sll.get(-1),
                "Negative index should throw exception"
        );

        assertThrows(
                IndexOutOfBoundsException.class,
                () -> sll.get(4),
                "Index out of range should throw exception"
        );
    }

    @Test
    void removeSLLTest() {
        sll.append('a');
        sll.append('b');
        sll.append('c');

        char item1 = sll.remove(1);

        assertEquals(
                'b',
                item1,
                "sll should be \"ac\", actual: \"" + sll + "\""
        );
        assertEquals(2, sll.getSize());

        char item0 = sll.remove(0);

        assertEquals(
                'a',
                item0,
                "sll should be \"c\", actual: \"" + sll + "\""
        );
        assertEquals(1, sll.getSize());
    }

    @Test
    void removeOutOfBoundsSLLTest() {
        assertThrows(
                IndexOutOfBoundsException.class,
                () -> sll.remove(10),
                "remove should throw IndexOutOfBoundsException"
        );
        assertThrows(
                IndexOutOfBoundsException.class,
                () -> sll.remove(-1),
                "remove should throw IndexOutOfBoundsException"
        );
    }

    @Test
    void appendSLLTest() {
        sll.append('a');
        assertEquals(
                'a',
                sll.get(sll.getSize() - 1),
                "sll should be \"a\", actual: \"" + sll + "\""
        );
        assertEquals(1, sll.getSize());
    }

    @Test
    void insertSLLTest() {
        sll.insert('b', 0);
        assertEquals('b', sll.get(0));
        assertEquals(1, sll.getSize());

        sll.insert('a', 0);
        assertEquals('a', sll.get(0));
        assertEquals(2, sll.getSize());

        sll.insert('c', 2);
        assertEquals('c', sll.get(2));
        assertEquals(3, sll.getSize());

        assertEquals(3, sll.getSize());

        assertThrows(
                IndexOutOfBoundsException.class,
                () -> sll.insert('d', 10),
                "insert should throw exception"
        );

        assertThrows(
                IndexOutOfBoundsException.class,
                () -> sll.insert('d', -1),
                "insert should throw exception"
        );
    }
}
