#include <iostream>

using namespace std;

/**
 * Write a program that use new to allocate the array dynamically for five integers
 * The five values will be stored in an array using a pointer
 * Print the elements of the array in reverse order using a pointer
*/

int main() {

    int* p1 = new int[5] {1, 2, 3, 4, 5};
    // Get the pointer of the last element
    int* p = p1 + 4;

    for(int i=0; i<5; i++, p--) {
        cout << "Index of element: " << (4-i) << endl;
        cout << *p << " " << p << endl;
    }

    return 0;
}