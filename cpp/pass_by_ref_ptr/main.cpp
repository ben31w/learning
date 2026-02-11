// g++ -c main.cpp && g++ -o main.exe main.o
#include <iostream>

#include "main.h"

using namespace std;

namespace Util {
    // Pass by value (no operator). 
    // A shallow copy of variable is passed.
    // Modifications made to the copy are not made to the orignal variable.
    // Safe, but copying can be expensive.
    void printX(int x) {
        cout << "printX: You passed in " << x << endl;
        x *= 2;
        cout << "printX: Doubling a copy: " << x << endl;
    }

    // Pass by reference (&)
    // A reference to the variable/the variable itself is passed.
    // No copying, modifications are permanent.
    void doubleX(int& x) {
        cout << "doubleX(int&): You passed in  " << x << endl;
        x *= 2;
        cout << "doubleX(int&): Doubling: " << x << endl;
    }

    // Pass by pointer (*)
    // A pointer to the variable is passed: pointer must be dereferenced
    // and null-checked. You can do pointer arithmetic though.
    // No copying, modifications are permanant.
    void doubleX(int* x) {
        if (x == nullptr) {
            cout << "doubleX(int*): nullptr, exiting " << endl;
            return;
        }

        cout << "doubleX(int*): You passed in " << *x << endl;
        *x *= 2;
        cout << "doubleX(int*): Doubling: " << *x << endl;
    }   
}


int main() {
    int i = 10;

    Util::printX(i);
    Util::doubleX(i);

    int* p = &i;

    Util::doubleX(p);

    cout << "---Final values---" << endl;
    cout << "i\t&i\t\tp\t\t&p\t\t*p" << endl;
    cout << i << '\t' << &i << '\t' << p << '\t' << &p << '\t' << *p << endl;

    return 0;
}