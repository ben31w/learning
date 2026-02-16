// g++ -c watch.cpp human.cpp main.cpp && g++ -o main.exe watch.o human.o main.o
// TODO this really needs a build tool
#include <iostream>

#include "human.h"
#include "watch.h"

using namespace std;

int main() {
    // In C++, declaring always instantiates an object (via default constructor)
    Time::Watch citizen;
    Time::Human placeholder;
    Time::Human ben("Ben");
    Time::Human dragos("Dragos", &citizen);

    cout << placeholder.getTime() << endl;
    cout << ben.getTime() << endl;
    cout << dragos.getTime() << endl;

    return 0;
}