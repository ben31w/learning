#pragma once

int main();

void passByVal(int i);

void passByRef(int& i);
void passByConstRef(const int& i);

void passByPtr(int* p);
void passByPtrToConst(const int* p);
void passByConstPtr(int* const p);
void passByConstPtrToConst(const int* const p);
