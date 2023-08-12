#include "../headers/functions.h"
#include <iostream>

using namespace std;

int main() {

    int n;

    cout << "Please input a positive number: ";
    cin >> n;

    if (n == 1) {
        cout << "1" << endl;
    }else if (n >= 2) {
        int* nums = new int[n];
        nums[0] = 1;
        nums[1] = 1;
        fib(2, nums, n);

        for(int i=0; i<n; i++) {
            cout << nums[i] << " ";
        }
        cout << endl;
    } else {
        cout << "Invalid number received" << endl;
    }

    return 0;
}