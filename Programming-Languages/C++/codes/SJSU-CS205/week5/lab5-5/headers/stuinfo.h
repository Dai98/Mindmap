// Header Guard 头文件防卫式声明
// This avoids linking failure
// When multiple cpp files imports the same header file
# pragma once

struct StuInfo {
    char name[20];
    double score[3];
    double average;
};

void inputStu(StuInfo stu[], int n);
void showStu(StuInfo stu[], int n);