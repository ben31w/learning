// g++ -c person.cpp && g++ -o person.exe person.o
#include <ctime>
#include <iostream>

#include "person.h"

using namespace std;

// =====PersonStruct====

PersonStruct::PersonStruct(const string& s, const time_t& t):
    fname(s),
    birthdate(t) { }

// =====PersonClass====

PersonClass::PersonClass(const string& s, const time_t& t):
    fname(s), 
    birthdate(t) { }

string PersonClass::getFName() {
    return fname;
}


int main() {
    PersonStruct personStruct("Anna", time(0));

    return 0;
}