#include <iostream>

using namespace std;

int main() {
    int n,fa;
    do{
        // n is not initialized
        // So the initial value of n is random
        // Always initialized the variables in C++!
        std::cout << fa << " " << n << endl;
        fa *= n;
        n++;
    }while(n <= 10);
    
    std::cout << "fa = " << fa << endl;
    
    return 0;
}