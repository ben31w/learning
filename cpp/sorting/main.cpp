// g++ -c main.cpp && g++ -o main.exe main.o
#include <algorithm>
#include <iostream>
#include <vector>

#include "main.h"

using namespace std;

struct SWE {
    string fname;
    string lname;
    int level;

    SWE(string fname, string lname, int level) : fname(fname), lname(lname), level(level) {}

    static bool compareFName(const SWE& left, const SWE& right) {
        return left.fname < right.fname;
    }

    static bool compareLName(const SWE& left, const SWE& right) {
        return left.lname < right.lname;
    }

    static bool compareLevel(const SWE& left, const SWE& right) {
        if (left.level == right.level) {
            return compareFName(left, right);
        }
        return left.level < right.level;
    }
};

namespace VUtil {
    void printVector(vector<SWE> v) {
        for (int i = 0; i < v.size(); i++) {
            SWE swe = v[i];
            cout << i+1 << ") " << swe.fname << ' ' << swe.lname << ", L" << swe.level << endl;
        }
    }
}

int main() {
    SWE ben("Ben", "Wright", 1);
    vector<SWE> swe_ls = {
        ben,
        SWE("Michael", "Petersen", 2),
        SWE("Chris", "Moore", 4),
        SWE("Jeremy", "Dorr", 4),
        SWE("Mohan", "Sunkavalli", 5)
    };

    sort(swe_ls.begin(), swe_ls.end(), SWE::compareFName);
    cout << "\n---Sorted by FName---" << endl;
    VUtil::printVector(swe_ls);

    sort(swe_ls.begin(), swe_ls.end(), SWE::compareLName);
    cout << "\n---Sorted by LName---" << endl;
    VUtil::printVector(swe_ls);

    sort(swe_ls.begin(), swe_ls.end(), SWE::compareLevel);
    cout << "\n---Sorted by Level---" << endl;
    VUtil::printVector(swe_ls);

    return 0;
}