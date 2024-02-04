#include "functions.h"
#include "dayInfo.h"
#include "enums.h"

bool canTravel(DayInfo dayInfo) {
    return dayInfo.weather == Sunny && (dayInfo.day == Sunday || dayInfo.day == Saturday);
}