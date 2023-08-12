#include <iostream>
using namespace std;


int main() {
    int a, b;
    double c, d;
    a = 19.99 + 21.99;
    b = (int)19.99 + (int)21.99;
    c = 23 / 8;
    d = 23 / 8.0;
    cout << "a = " << a << endl;  // a is 41, 41.98 will be converted to 41, then assigned to a
    cout << "b = " << b << endl;  // b is 40, 19 + 21 = 40
    cout << "c = " << c << endl;  // c is 2, because 23 and 8 are all integers
    cout << "d = " << d << endl;  // d is 2.875
    cout << "0/0= " << 0/0 << endl;  // 0/0 is nan
    return 0;
}
