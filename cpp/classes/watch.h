#pragma once

//////////////////
// GENERAL HEADER FILE RULES
//////////////////

// Header files can (and should) include other files.
// Include guards (pragma) should prevent duplicate imports.

#include <string>

// Never add `using namespace` inside any header file.

//////////////////
// "CLASS-TYPE" HEADER FILE RULES
//////////////////

//  - Wrap classes in a namespace
//  - `class` keyword is only for header files
//      - Declare public methods (including constructors and destructors)
//      - Declare private fields and helper methods
//  - In general, header files are for declarations (signatures) and cpp files
//    are for implementations. But simple implementations are okay inside headers.

namespace Time {
    class Watch {
        public:
            Watch();
            std::string getTime();
    };
}

