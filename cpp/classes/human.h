#pragma once

#include <string>

#include "watch.h"

namespace Time {
    class Human {
        private:
            // --fields--
            std::string name;
            Time::Watch *watch;
            // Could also define
            // --helper methods--
            // --private constructors--
        
        public:
            // --constructors--
            // Interestingly, you don't need to specify argument names here.
            // Only types are required.
            Human();
            Human(const std::string&);
            Human(const std::string& n, Time::Watch* w);
            // --methods--
            std::string getTime();
            int add(int, int);
    };
}

