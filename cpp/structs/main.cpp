#include <iostream>

#include "main.h"

using namespace std;

string PersonClass::getFName() {
    return fname;
}

int main() {
    PersonStruct personStruct;
    PersonClass personClass;

    cout << personStruct.fname << endl;
    cout << personClass.getFName() << endl;

    return 0;
}