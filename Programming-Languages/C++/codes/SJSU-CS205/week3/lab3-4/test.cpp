#include <iostream>

using namespace std;

int main() {
    int num;
    int num2;
    int num3;
    int num4;
    int num5;
    int num6;
    int num7;
    int num8;
    int num9;
    int num10;

    // It is true that uninitialized integer might have random values
    // The random value depends on what is left in the address of the memory
    // But for modern OS, it is more common to have 0 in the memory
    // But Note that this is not guaranteed, always initialize your variables!

    std::cout << "num = " << num << endl;
    std::cout << "num2 = " << num2 << endl;
    std::cout << "num3 = " << num3 << endl;
    std::cout << "num4 = " << num4 << endl;
    std::cout << "num5 = " << num5 << endl;
    std::cout << "num6 = " << num6 << endl;
    std::cout << "num7 = " << num7 << endl;
    std::cout << "num8 = " << num8 << endl;
    std::cout << "num9 = " << num9 << endl;
    std::cout << "num10 = " << num10 << endl;

    return 0;
}