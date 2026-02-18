// g++ -c person.cpp && g++ -o person.exe person.o
#include <chrono>
#include <ctime>
#include <iostream>

#include "person.h"

// Structs and classes have the same semantics.

// =====PersonStruct====

PersonStruct::PersonStruct(const std::string& s, const std::tm& t):
    fname(s),
    birthdate(t) { }

int PersonStruct::getAge() 
{
    return 1;
}

// =====PersonClass====

PersonClass::PersonClass(const std::string& s, const std::tm& t):
    fname(s), 
    birthdate(t) { }

int PersonClass::getAge()
{
    // Turns out this is a PITA in C++, so I'm not going to bother
    return 1;
}


int main()
{
    // C++ has multiple datetime types:
    // - time_t - simple timestamp, seconds since 1970
    // - struct tm - datetime structure
    // - std::chrono::time_point
    // - std::chrono::year_month_day - C++20 must be enabled
    tm bday;
    bday.tm_year = 2002;
    bday.tm_mon = 2;
    bday.tm_mday = 13;

    PersonStruct ben("Ben", bday);
    PersonClass bw("Ben", bday);

    std::cout << bw.getAge() << std::endl;

    return 0;
}