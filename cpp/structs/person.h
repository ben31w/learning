#pragma once

#include <ctime>
#include <string>

// Structs are public by default
struct PersonStruct {
    std::string fname;
    std::time_t birthdate;

    // To use string literals in a constructor with pass by ref, use const
    PersonStruct(const std::string& s, const std::time_t& t);
    int getAge();
};

// Classes are private by default
class PersonClass {
    private:
        std::string fname;
        std::time_t birthdate;
    public:
        PersonClass(const std::string& s, const std::time_t& t);
        std::string getFName();
        int getAge();
};

int main();
