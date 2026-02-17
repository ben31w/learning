// g++ -c main.cpp && g++ -o main.exe main.o
#include <iostream>

#include "main.h"

using namespace std;

// Syntax              Term                            Desc
// T arg               Pass by value                   shallow copy is passed; OG var isn't modified
// T& arg              Pass by reference               OG var is passed and modified. Reference to OG var = OG var.
// const T& arg        Pass by const reference         OG var is passed but not modified.
// T* arg              Pass by pointer                 copy of pointer to OG var is passed. Pointer copy and var pointed to are modified.
// const T* arg        Pass by pointer to const        copy of pointer to OG var is passed. Pointer copy can be modified; var pointed to cannot.
// T* const arg        Pass by const pointer           copy of pointer to OG var is passed. Pointer copy cannot be modified; var pointed to can.
// const T* const arg  Pass by const pointer to const  copy of pointer to OG var is passed. Pointer copy and var pointed to cannot be modified.

// T** arg              Pass by pointer to pointer                      pointer to pointer to OG var is passed. Pointer and var pointed to are modified.
// T*& arg              Pass by reference to pointer                    pointer to OG var is passed. Pointer and var pointed to are modified. Preferred.
// const T*& arg        Pass by reference to pointer to const           pointer to OG var is passed. Pointer can be modified; var pointed to cannot.
// const T* const& arg  Pass by reference to const pointer to const     pointer to OG var is passed. Pointer and var pointed to cannot be modified.

// NOTES
// - Pass by value is rarely used because copying can be expensive.
//   If you want to avoid modifications to OG var, use const reference, pointer to const, or const pointer to const.
// - Note, pass by pointer really passes a copy to a pointer. Similar to pass by value. The pointer can be re-assigned,
//   but only temporarily, because it's a copy. To access the pointer itself, pass by reference to pointer.

void passByVal(int i)
{
    i += 1; // modifies a copy.
}

void passByRef(int &i)
{
    i += 1; // modifies OG var
}

void passByConstRef(const int &i)
{
    // i += 1;  // not allowed
}

void passByPtr(int *p)
{
    if (p == nullptr) return;
    
    *p += 1; // de-references ptr to modify OG var
}

void passByPtrToConst(const int *p)
{
    if (p == nullptr) return;
    
    // *p += 1;  // not allowed
}

void passByConstPtr(int *const p)
{
    if (p == nullptr) return;
    
    *p += 1; // de-references ptr to modify OG var
}

void passByConstPtrToConst(const int *const p)
{
    if (p == nullptr) return;
    
    // *p += 1;  // not allowed
}

void passByPtrToPtr(int **p)
{
    if (p == nullptr) return;

    static int x = 20;
    *p = &x;
    **p += 1;
}

void passByRefToPtr(int*& p)
{
    if (p == nullptr) return;

    static int x = 30;
    p = &x;
    *p += 1;
}

void passByRefToPtrToConst(const int*& p) {
    if (p == nullptr) return;

    static int x = 40;
    p = &x;
    // *p += 1;  // not allowed
}

void passByRefToConstPtrToConst(const int* const& p) {
    if (p == nullptr) return;

    static int x = 40;
    // p = &x;  // not allowed
    // *p += 1;  // not allowed
}

void demoPass()
{
    cout << "\n====Pass variables and references: pointers don't change.====" << endl;

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
}

void demoPassFancy()
{
    cout << "\n====Pass pointer variables: pointers change.====" << endl;

    int i = 10;
    int *p = &i;

    cout << "----initialize----" << endl;
    cout << "   i = " << i << endl;
    cout << "  *p = " << *p << endl;

    passByPtrToPtr(&p);

    cout << "----passByPtrToPtr----" << endl;
    cout << "   i = " << i << endl;
    cout << "  *p = " << *p << endl;

    passByRefToPtr(p);

    cout << "----passByRefToPtr----" << endl;
    cout << "   i = " << i << endl;
    cout << "  *p = " << *p << endl;

    // passByRefToPtrToConst(p);

    // cout << "----passByRefToPtrToConst----" << endl;
    // cout << "   i = " << i << endl;
    // cout << "  *p = " << *p << endl;

    passByRefToConstPtrToConst(p);

    cout << "----passByRefToConstPtrToConst----" << endl;
    cout << "   i = " << i << endl;
    cout << "  *p = " << *p << endl;
}

int main()
{
    demoPass();

    demoPassFancy();

    return 0;
}