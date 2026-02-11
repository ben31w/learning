// g++ -c main.cpp && g++ -o main.exe main.o
#include <iostream>

#include "main.h"

using namespace std;

int main() {
    // A reference variable is an alias for another variable.
    // The address of the reference is the same as the address of the OG var.
    // It's the same variable, not a copy.
    
    int i = 10;
    int& r = i;

    cout << "---Init variable and reference---" << endl;
    cout << "i\tr\t&i\t\t&r" << endl;
    cout << i << '\t' << r << '\t' << &i << '\t' << &r << endl;

    // Editing the reference is the same as editing the OG var. They are the same.

    i = 20;

    cout << "---Edit variable---" << endl;
    cout << "i\tr\t&i\t\t&r" << endl;
    cout << i << '\t' << r << '\t' << &i << '\t' << &r << endl;

    r = 30;

    cout << "---Edit reference---" << endl;
    cout << "i\tr\t&i\t\t&r" << endl;
    cout << i << '\t' << r << '\t' << &i << '\t' << &r << endl;

    // A pointer variable stores the memory address of another variable.
    // To access the OG var via a pointer, you must dereference it with '*'.
    // The only benefit to pointers is they enable pointer (memory address) arithmetic.

    int* p = &i;

    cout << "---Init pointer---" << endl;
    cout << "i\tr\t&i\t\t&r\t\tp\t\t*p\t&p" << endl;
    cout << i << '\t' << r << '\t' << &i << '\t' << &r << '\t' << p << '\t' << *p << '\t' << &p << '\t' << endl;

    *p = 40;

    cout << "---Edit pointer---" << endl;
    cout << "i\tr\t&i\t\t&r\t\tp\t\t*p\t&p" << endl;
    cout << i << '\t' << r << '\t' << &i << '\t' << &r << '\t' << p << '\t' << *p << '\t' << &p << '\t' << endl;

    i = 50;

    cout << "---Edit variable again---" << endl;
    cout << "i\tr\t&i\t\t&r\t\tp\t\t*p\t&p" << endl;
    cout << i << '\t' << r << '\t' << &i << '\t' << &r << '\t' << p << '\t' << *p << '\t' << &p << '\t' << endl;

    // Bonus:
    // * as unary operator is pointer dereference.
    // * as binary operator is multiplication.

    *p = *p * 2;

    cout << "---Edit pointer again---" << endl;
    cout << "i\tr\t&i\t\t&r\t\tp\t\t*p\t&p" << endl;
    cout << i << '\t' << r << '\t' << &i << '\t' << &r << '\t' << p << '\t' << *p << '\t' << &p << '\t' << endl;

    // You can do itelligent logic with pointer arithmetic, ex: iteration.
    // Here, we just increment the pointer and get a random value from memory every time.

    ++p;

    cout << "---Increment pointer---" << endl;
    cout << "i\tr\t&i\t\t&r\t\tp\t\t*p\t&p" << endl;
    cout << i << '\t' << r << '\t' << &i << '\t' << &r << '\t' << p << '\t' << *p << '\t' << &p << '\t' << endl;


    return 0;    
}