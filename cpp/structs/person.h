#pragma once

#include <ctime>
#include <string>

// Structs are public by default
struct PersonStruct {
    std::string fname;
    std::tm birthdate;

    // To use string literals in a constructor with pass by ref, use const
    PersonStruct(const std::string& s, const std::tm& t);
    int getAge();
};

// Classes are private by default
class PersonClass {
    private:
        std::string fname;
        std::tm birthdate;
    public:
        // To use string literals in a constructor with pass by ref, use const
        PersonClass(const std::string& s, const std::tm& t);
        std::string getFName() { return fname; }
        int getAge();
};

int main();
