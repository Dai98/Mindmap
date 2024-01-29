#include <iostream>

using namespace std;

int main() {
    int n = 5;
    int sum;
    
    while(n > 0){
        sum += n;
        // while loop will never stop
        // Because n never changes
        cout << "n = " << n << " ";
        cout << "sum = " << sum << " ";
    }
    
    return 0;
}
