#include <iostream>

using namespace std;

int main() {
    //int count = 0;
    // for(size_t n = 2; n >= 0; n--) {

    // size_t is unsigned integer, so it doesn't have negative values (0-1=18446744073709551615)
    // so for loop never ends
    // use int in for loop
    for(int n = 2; n >= 0; n--) {
        std::cout << "n = " << n << " ";
        // std::cout << (n >= 0) << endl;
        // count++;
        // if (count == 4) {
        //     break;
        // }
    }
    return 0;
}