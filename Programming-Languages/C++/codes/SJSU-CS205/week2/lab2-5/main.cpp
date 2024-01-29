#include <iostream>
int main(){
    auto a = 10;  // a is int and equals to 10
    a = 20.5;     // a is 20 (20.5 is converted to 20 and assigned to a)
    a += 10.5;    // a = a + 10.5, 30.5 will be converted to 30 and assigned to a
    // a is 30
    std::cout << a << std::endl;
    return 0;
}