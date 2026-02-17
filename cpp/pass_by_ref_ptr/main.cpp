// g++ -c main.cpp && g++ -o main.exe main.o
#include <iostream>

#include "main.h"

using namespace std;

//  Syntax              Term                            Desc
//  T arg               Pass by value                   shallow copy is passed; OG var isn't modified
//  T& arg              Pass by reference               OG var is passed and modified. Reference to OG var = OG var.
//  const T& arg        Pass by const reference         OG var is passed but not modified.
//  T* arg              Pass by pointer                 pointer to OG var is passed. Pointer and variable pointed to are modified.
//  const T* arg        Pass by pointer to const        pointer to OG var is passed. Pointer can be modified; variable pointed to cannot.
//  T* const arg        Pass by const pointer           pointer to OG var is passed. Pointer cannot be modified; variable pointed to can.
//  const T* const arg  Pass by const pointer to const  pointer to OG var is passed. Pointer and variable pointed to cannot be modified.

// Pass by value is rarely used because copying can be expensive.
// If you want to avoid modifications to OG var, use const reference, pointer to const, or const pointer to const.

void passByVal(int i) {
    i += 1;  // modifies a copy.
}

void passByRef(int& i) {
    i += 1;  // modifies OG var
}

void passByConstRef(const int& i) {
    // i += 1;  // not allowed
}

void passByPtr(int* p) {
    if (p == nullptr) {
        return;
    }
    *p += 1;  // de-references ptr to modify OG var
}

void passByPtrToConst(const int* p) {
    if (p == nullptr) {
        return;
    }
    // *p += 1;  // not allowed
}

void passByConstPtr(int* const p) {
    if (p == nullptr) {
        return;
    }
    *p += 1;  // de-references ptr to modify OG var
}

void passByConstPtrToConst(const int* const p) {
    if (p == nullptr) {
        return;
    }
    // *p += 1;  // not allowed
}


int main() {
    int i = 10;

    cout << "----initialization----" << endl;
    cout << "i=" << i << endl;

    passByVal(i);

    cout << "----passByVal----" << endl;
    cout << "i=" << i << endl;

    passByRef(i);

    cout << "----passByRef----" << endl;
    cout << "i=" << i << endl;

    passByConstRef(i);

    cout << "----passByConstRef----" << endl;
    cout << "i=" << i << endl;

    passByPtr(&i);

    cout << "----passByPtr----" << endl;
    cout << "i=" << i << endl;

    passByPtrToConst(&i);

    cout << "----passByPtrToConst----" << endl;
    cout << "i=" << i << endl;

    passByConstPtr(&i);

    cout << "----passByConstPtr----" << endl;
    cout << "i=" << i << endl;

    passByConstPtrToConst(&i);

    cout << "----passByConstPtrToConst----" << endl;
    cout << "i=" << i << endl;

    return 0;
}