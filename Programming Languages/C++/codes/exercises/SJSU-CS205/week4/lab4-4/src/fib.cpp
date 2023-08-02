#include "../headers/functions.h"
#include <iostream>

using namespace std;

void fib(int n, int* nums, int length) {
    if (length == n) {
        return;
    }

    nums[n] = nums[n-1] + nums[n-2];

    fib(n+1, nums, length);
}