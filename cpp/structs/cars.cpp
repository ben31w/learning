// g++ -c cars.cpp && g++ -o cars.exe cars.o
#include <iostream>

#include "cars.h"

using namespace std;

// Unnamed structs
// Less flexible, harder to define instances
struct {
    string make;
    string model;
    int year;

    string str() {
        return to_string(year) + " " + make + " " + model;
    }
} car1, car2;

int main() {
    car1.make = "Hyundai";
    car1.model = "Santa Fe";
    car1.year = 2011;

    cout << car1.str() << endl;

    return 0;
}