#include <iostream>
using namespace std;

int main() {
    cout << fixed;
    float f1 = 1.0f;
    cout<<"f1 = "<<f1<<endl;

    float a = 0.1f;
    float f2 = a+a+a+a+a+a+a+a+a+a;
    // f2 = 1.0
    cout<<"f2 = "<<f2<<endl;

    // f1 != f2
    // because adding 0.1f 10 times will accumulate small errors and 
    if(f1 == f2)
        cout << "f1 = f2" << endl;
    else
        cout << "f1 != f2" << endl;

    return 0;
}
