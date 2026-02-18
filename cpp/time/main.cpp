// g++ -std=c++20 -c main.cpp && g++ -std=c++20 -o main.exe main.o
#include <chrono>
#include <iostream>

int main() {
    using namespace std::chrono;
    year_month_day ymd{year{2026}, month{2}, day{17}};
    std::cout << ymd << std::endl;
}
