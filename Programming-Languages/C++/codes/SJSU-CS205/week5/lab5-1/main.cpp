#include <iostream>
using namespace std;

int main() {
    char *pc, cc = 'A';
    int *pi, ii = 10;
    float *pf, ff = 23.4f;
    double *pd, dd = 123.78;

    pc = &cc;
    pi = &ii;
    pf = &ff;
    pd = &dd;

    // The length of pointer is determined by operating system
    // As of now (2023), most computers are 64-bit, which means pointers on these computers have 64 bits (8 bytes)
    // char type has 8 bits (1 byte), and its pointer has 8 bytes
    cout << "sizeof(cc) = " << sizeof(cc) << ", sizeof(pc) = " << sizeof(pc) << endl;
    // int type has 32 bits (4 byte), and its pointer has 8 bytes
    cout << "sizeof(ii) = " << sizeof(ii) << ", sizeof(pi) = " << sizeof(pi) << endl;
    // float type has 32 bits (4 byte), and its pointer has 8 bytes
    cout << "sizeof(ff) = " << sizeof(ff) << ", sizeof(pf) = " << sizeof(pf) << endl;
    // double type has 64 bits (8 byte), and its pointer has 8 bytes
    cout << "sizeof(dd) = " << sizeof(dd) << ", sizeof(pd) = " << sizeof(pd) << endl;

    // Pointers are hexadecimal integers, and they have addresses too (&p) 
    cout << "&pc = " << &pc << ", pc = " << static_cast <void*>(pc) << ", *pc = " << *pc << endl;
    cout << "&pi = " << &pi << ", pi = " << pi << ", *pi = " << *pi << endl;
    cout << "&pf = " << &pf << ", pf = " << pf << ", *pf = " << *pf << endl;
    cout << "&pd = " << &pd << ", pd = " << pd << ", *pd = " << *pd << endl;

    const char *msg = "C/C++ programming is fun.";
    const char *copy;

    // msg is the address of the first element in the char array (C)
    // when running copy = msg;, copy is also assigned with the address of the first element
    // therefore, copy and msg are two integer variables with same values
    // But since they are two separate variables, they have different addresses
    copy = msg;
    cout << "msg = " << msg << ",its address is: " << (void*)msg << ", &msg = " << &msg << endl;
    cout << "copy= " << copy << ",its address is: " << (void*)copy << ", &copy= " << &copy << endl;
    
    return 0;
}
