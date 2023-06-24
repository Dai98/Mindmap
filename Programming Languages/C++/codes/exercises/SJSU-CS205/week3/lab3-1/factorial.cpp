#include "functions.h"

int factorial(int n) {
    // End recursion
    if (n == 1)
        return 1;
    else
        // Calculate factorial recursively
        return n * factorial(n - 1);
}