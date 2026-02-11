// g++ -c hello.cpp && g++ -o hello.exe hello.o
#include <iostream>

#include "hello.h"

using namespace std;

namespace HelloUtil {
    void printHello() {
        cout << "Hello World" << endl;
    }
}

int main() {
    HelloUtil::printHello();
    return 0;
}