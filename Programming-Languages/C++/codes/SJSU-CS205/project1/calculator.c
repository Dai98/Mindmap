#include <stdio.h>
#include "str_util.h"

int main(int argc, char *argv[]) {
    char *firstNum = argv[1];
    char *operator = argv[2];
    char *secondNum = argv[3]; 
    
    char* test = "    Hello World    ";

    printf("test length: %d", str_len(test));
    printf("test: ==%s==", test);
    printf("test length after strip: %d", str_len(strip(test)));
    printf("test: ==%s==", strip(test));

    return 0;
}

