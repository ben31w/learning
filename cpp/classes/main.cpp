// g++ -c watch.cpp main.cpp && g++ -o main.exe watch.o main.o
// TODO this really needs a build tool
#include <iostream>

#include "watch.h"

using namespace std;

int main() {
    // In C++, declaring always instantiates an object (via default constructor)
    Time::Watch citizen;
    Time::Watch rolex;

    cout << citizen.getTime() << endl;

    return 0;
}