#include <stdio.h>
int main(){
    signed char a = 127;
    unsigned char b = 0xff;
    unsigned char c = 0;
    a++;
    b++;
    c--;
    // a=-128  a = 01111111 => a++ => a = 10000000 => -128 (Two's Complement)
    // b=0  b=11111111(binary) => b++ => 1/00000000 => 00000000 overflow  
    // c=255  0-1=-1, -1's Two Complement is 11111111, for a unsigned integer, it becomes 255
    printf("a=%d\nb=%d\nc=%d\n",a,b,c);
    return 0;
}