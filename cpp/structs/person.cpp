// g++ -c person.cpp && g++ -o person.exe person.o
#include <chrono>
#include <ctime>
#include <iostream>

#include "person.h"


// Source - https://stackoverflow.com/a/16784256
// Posted by Howard Hinnant, modified by community. See post 'Timeline' for change history
// Retrieved 2026-02-18, License - CC BY-SA 4.0

template <class Duration>
std::tm
make_utc_tm(std::chrono::time_point<std::chrono::system_clock, Duration> tp)
{
    using namespace std;
    using namespace std::chrono;
    typedef duration<int, ratio_multiply<hours::period, ratio<24>>> days;
    // t is time duration since 1970-01-01
    Duration t = tp.time_since_epoch();
    // d is days since 1970-01-01
    days d = round_down<days>(t);
    // t is now time duration since midnight of day d
    t -= d;
    // break d down into year/month/day
    int year;
    unsigned month;
    unsigned day;
    std::tie(year, month, day) = civil_from_days(d.count());
    // start filling in the tm with calendar info
    std::tm tm = {0};
    tm.tm_year = year - 1900;
    tm.tm_mon = month - 1;
    tm.tm_mday = day;
    tm.tm_wday = weekday_from_days(d.count());
    tm.tm_yday = d.count() - days_from_civil(year, 1, 1);
    // Fill in the time
    tm.tm_hour = duration_cast<hours>(t).count();
    t -= hours(tm.tm_hour);
    tm.tm_min = duration_cast<minutes>(t).count();
    t -= minutes(tm.tm_min);
    tm.tm_sec = duration_cast<seconds>(t).count();
    return tm;
}


// Structs and classes have the same semantics.

// =====PersonStruct====

PersonStruct::PersonStruct(const std::string& s, const std::tm& t):
    fname(s),
    birthdate(t) { }

int PersonStruct::getAge() 
{
    return 1;
}

// =====PersonClass====

PersonClass::PersonClass(const std::string& s, const std::tm& t):
    fname(s), 
    birthdate(t) { }

int PersonClass::getAge()
{
    const auto now = std::chrono::system_clock::now();
    tm tm_now = make_utc_tm(now);

    // Subtract birthdate as seconds since 1970 from current time as seconds since 1970,
    // then convert seconds to years.

    // Probably better ways to do this. year_month_day seems promising


    return tm_now.tm_year - birthdate.tm_year;
}


int main()
{
    // C++ has multiple datetime types:
    // - time_t - simple timestamp, seconds since 1970
    // - struct tm - datetime structure
    // - std::chrono::time_point
    // - std::chrono::year_month_day - C++20 must be enabled
    tm bday;
    bday.tm_year = 2002;
    bday.tm_mon = 2;
    bday.tm_mday = 13;

    PersonStruct ben("Ben", bday);
    PersonClass bw("Ben", bday);

    std::cout << bw.getAge() << std::endl;

    return 0;
}