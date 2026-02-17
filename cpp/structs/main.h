#pragma once

#include <string>

struct PersonStruct {
    std::string fname;
    // add birthday
};

class PersonClass {
    private:
        std::string fname;
    public:
        std::string getFName();
};

int main();
