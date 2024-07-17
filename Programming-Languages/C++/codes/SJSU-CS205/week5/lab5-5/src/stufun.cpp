#include "stuinfo.h"
#include <iostream>

void inputStu(StuInfo stu[], int n) {
    for(int i=0; i<n; i++) {
        std::cout << "Input information for student " << (i+1) << ": " << std::endl;
        std::cout << "    Input name of this student: ";
        std::cin >> stu[i].name;

        for(int j=0; j<=2; j++) {
            std::cout << "    Input score" << (j+1) << " of this student: ";
            std::cin >> stu[i].score[j];
        }

        stu[i].average = (stu[i].score[0] + stu[i].score[1] + stu[i].score[2]) / 3;
    }
}

void showStu(StuInfo stu[], int n) {
    struct StuInfo * stuPointer = stu;
    for(int i=0; i<n; i++, stuPointer++) {
        std::cout << "Student " << (i+1) << ": " << std::endl;
        std::cout << "    Name: " << stuPointer->name << std::endl;
        std::cout << "    Score1: " << stuPointer->score[0] << std::endl;
        std::cout << "    Score2: " << stuPointer->score[1] << std::endl;
        std::cout << "    Score3: " << stuPointer->score[2] << std::endl;
        std::cout << "    Average: " << stuPointer->average << std::endl;
    }
}