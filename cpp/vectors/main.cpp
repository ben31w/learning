// g++ -c main.cpp && g++ -o main.exe main.o
#include <iostream>
#include <vector>

#include "main.h"

using namespace std;

namespace VUtil {
    // print vector with simple for loop
    void printVector(vector<char> v) {
        for (int i = 0; i < v.size(); i++) {
            cout << v[i] << ' ';
        }
        cout << endl;
    }

    // print vector the "fancy way" using
    //     o=.                  o.o
    //  o  o++E                    .= E.
    // + . Ooo.    *iterators*    .B.o     
    //  + O B..                       .= 
    //   = *S.                    S   = .
    void printVectorFancy(vector<char> v) {
        vector<char>::iterator iter;
        for (iter = v.begin(); iter < v.end(); iter++) {
            cout << *iter << ' ';
        }
        cout << endl;
    }

    // Insert char c before given pos.
    // Pass by reference to modify v directly.
    void insertInto(std::vector<char>& v, int pos, char c) {
        vector<char>::iterator iter = v.begin();
        for (int i = 0; i < pos; i++) {
            ++iter;
        }
        v.insert(iter, c);
    }
}

int main() {
    vector<char> v = {'b', 'w'};
    VUtil::printVector(v);

    VUtil::insertInto(v, 1, 'n');
    VUtil::insertInto(v, 2, 'd');

    VUtil::printVectorFancy(v);
    return 0;
}