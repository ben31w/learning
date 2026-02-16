#include <ctime>

#include "watch.h"

using namespace std;

//////////////////
// "CLASS-TYPE" CPP FILE RULES
//////////////////

// Wrap the class's methods in the same namespace that the header defines.
// Scope methods to the class with `rtype ClassName::method`

namespace Time {
    // ----Constructors----
    // A constructor is a special method that is automatically called 
    // when an object is created.

    // Constructors don't have an rtype (not even void).

    // In C++, the default constructor is called even when an object is simply declared.
    // Ex: 
    //      Watch myWatch;  // instantiates a Watch
    // This is unlike Java, where objects can be declared without being instantiated.

    Watch::Watch() { }

    // ----Methods----
    // `rtype ClassName::method`

    string Watch::getTime() {
        time_t now = time(0);
        char* date_time = ctime(&now);
        return date_time;
    }
}

