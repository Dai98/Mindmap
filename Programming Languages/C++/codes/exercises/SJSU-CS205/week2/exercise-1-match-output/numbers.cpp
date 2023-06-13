#include <iostream>

using std::cout;
using std::endl;

int main() {
    int num1 = 1234567890;
    int num2 = 1234567890;
    // overflow
    int sum = num1 + num2;
    cout << "sum = " << sum << endl;

    float f1 = 1234567890.0f;
    float f2 = 1.0f;
    float fsum = f1 + f2;
    // Rounding error
    cout << "fsum = " << fsum << endl;
    // Their difference is smaller than std::numeric_limits<float>::epsilon()
    cout << "(fsum == f1) is " << (fsum == f1) << endl;

    float f = 0.1f;
    float sum10x = f + f + f + f + f + f + f + f + f + f;
    float mul10x = f * 10;

    cout<<"sum10x = "<< sum10x << endl;
    cout<<"mul10x = "<< mul10x << endl;
    // Error of multiplication by 10 is smaller than adding 0.1 for 10 times
    cout<<"(sum10x == 1) is "<< (sum10x == 1.0) << endl;
    cout<<"(mul10x == 1) is "<< (mul10x == 1.0) << endl;
    return 0;
}