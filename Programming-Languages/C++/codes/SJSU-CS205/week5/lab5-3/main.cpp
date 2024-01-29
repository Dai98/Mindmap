#include <iostream>
using namespace std;

int main() {
    /**
     * a is actually
     * [[1, 3, 5, 7],
     *  [9, 11, 13, 15],
     *  [17, 19, 0, 0]]
    */
    int a[][4]={1,3,5,7,9,11,13,15,17,19}; 
    // Add/Substraction on pointer of 2-dim array will move on the first dimension
    // a+1 is the pointer to the second row/subarray in a ([9, 11, 13, 15])
    // *(a+1) gets the actual array value with the pointer
    // And since an array itself can be used as a pointer, it can be used to assign a pointer variable
    // Right now p points to the first element in the second subarray of a (namely 9)
    int *p=*(a+1);
    // Now p points to the fourth element in the second subarray of a (15)
    p += 3;
    // Here it retrieve the value that p points to (15) and do a self-increment
    // p points to the next element in the array, which goes to the first element in the third subarray (17)
    // 2-dimension arrays are still stored as 1-dimension array in memory
    // So pointers can move across the second dimension
    cout << "*p++ = " << *p++ << ",*p = " << *p << endl; 

    // pc is a pointer on a constant string
    const char *pc = "Welcome to programming.", *r;
    long *q = (long *)pc;
    // Since long is at least 4-byte long, and char is 1-byte long
    // So when q does self-increment, it moves 4 bytes forward
    q++;           
    // When it is converted back to char pointer
    // 4 characters are skipped from the start
    r = (char *)q;
    cout << r << endl;

    // m is an int, which is 4 byte long
    unsigned int m = 0x3E56AF67;
    // short is 2 byte long
    // So when the pointer to m is converted to short, only the smaller half is saved
    // Since my system is little endian
    unsigned short *pm = (unsigned short *) &m;
    cout << "*pm = " << hex << *pm << endl;
    
    return 0;
}
