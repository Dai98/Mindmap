#include "stuinfo.h"
#include <iostream>

using namespace std;

int main() {

    int n = 0;
    cout << "Please input how many students do you want to input: ";
    cin >> n;
    cout << endl;

    struct StuInfo* stu = new StuInfo[n];
    inputStu(stu, n);
    showStu(stu, n);

    return 0;
}