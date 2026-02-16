#include "human.h"

using namespace std;

namespace Time {
    // --constructors + fields--
    // fields are set alongside signature, not inside body.
    Human::Human(): 
        name("NoName"),
        watch(nullptr) { }

    Human::Human(const string& n):
        name(n),
        watch(nullptr) { }

    Human::Human(const string& n, Time::Watch* w):
        name(n),
        watch(w) { }

    // --methods--
    string Human::getTime() {
        if (watch == nullptr) {
            return name + ": I don't have a watch :/";
        }
        string result = name + ": " + watch->getTime();
        result +=       name + ": " + (*watch).getTime();
        return result;
    }

    int add(int a, int b) {
        return a + b;
    }

    // --helper methods--
}