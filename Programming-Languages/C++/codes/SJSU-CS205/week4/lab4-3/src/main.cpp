#include <iostream>
#include "functions.h"
#include "enums.h"
#include "dayInfo.h"

using namespace std;


int main() {
    struct DayInfo dayInfo1 = {Sunday, Sunny};
    struct DayInfo dayInfo2 = {Monday, Cloudy};
    struct DayInfo dayInfo3 = {Sunday, Rainy};

    cout << "DayInfo1, canTravel: " << canTravel(dayInfo1) << endl; 
    cout << "DayInfo2, canTravel: " << canTravel(dayInfo2) << endl; 
    cout << "DayInfo3, canTravel: " << canTravel(dayInfo3) << endl; 

    return 0;
}