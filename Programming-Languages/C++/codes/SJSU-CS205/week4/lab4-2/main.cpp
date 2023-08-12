#include <stdio.h>

union data {
    int n;
    char ch;
    short m;
};

int main() {

    /**
     * Output:
        4, 4
        40, @, 40
        39, 9, 39
        2059, Y, 2059
        3E25AD54, T, AD54
    */
    
    union data a;
    // The largest member is integer (32 bits, 4 bytes), so both output is 4
    // Most memory system uses an ascending index, so
    // index:     0        1        2        3
    // int  : ======== ======== ======== ========
    // char : ======== xxxxxxxx xxxxxxxx xxxxxxxx
    // short: ======== ======== xxxxxxxx xxxxxxxx
    printf("%d, %d\n", sizeof(a), sizeof(union data) );
    
    // 0x40=64
    // a.n = 0x40 pass value to the integer, which is large enough for n and m to store the whole number
    // @ is ASCII character with 64
    // Right now the memory is:
    // index:     0        1        2        3
    // int  : 01000000 ======== ======== ========
    // char : 01000000 xxxxxxxx xxxxxxxx xxxxxxxx
    // short: 01000000 ======== xxxxxxxx xxxxxxxx
    a.n = 0x40;
    printf("%X, %c, %hX\n", a.n, a.ch, a.m);
    
    // a.ch = '9' pass character to the char member, which is 39 in hexadecimal
    // Right now the memory is:
    // index:     0        1        2        3
    // int  : 00100111 ======== ======== ========
    // char : 00100111 xxxxxxxx xxxxxxxx xxxxxxxx
    // short: 00100111 ======== xxxxxxxx xxxxxxxx
    a.ch = '9';
    printf("%X, %c, %hX\n", a.n, a.ch, a.m);
    
    // a.m = 0x2059 pass 00100000 01011001 to all members
    // int and short are large enough to hold the values,
    // char can only store 01011001 in memory, since it only has 8 bits
    // which is 89 in decimal, and character 'Y' in ASCII 
    // Right now the memory is:
    // index:     0        1        2        3
    // int  : 01011001 00100000 ======== ========
    // char : 01011001 xxxxxxxx xxxxxxxx xxxxxxxx
    // short: 01011001 00100000 xxxxxxxx xxxxxxxx
    a.m = 0x2059;
    printf("%X, %c, %hX\n", a.n, a.ch, a.m);
    
    // a.m = 0x3E25AD54 pass 00111110 00100101 10101101 01010100 to all members
    // only int large enough to hold the values,
    // char can only store 01010100 in memory, since it only has 8 bits
    // which is 84 in decimal, and character 'T' in ASCII
    // short can only store 10101101 01010100, which is AD54 in hexadecimal
    // Right now the memory is:
    // index:     0        1        2        3
    // int  : 01010100 10101101 00100101 00111110
    // char : 01010100 xxxxxxxx xxxxxxxx xxxxxxxx
    // short: 01010100 10101101 xxxxxxxx xxxxxxxx
    a.n = 0x3E25AD54;
    printf("%X, %c, %hX\n", a.n, a.ch, a.m);

    // With all the analysis above
    // My computer is proved to be little endian

    return 0;
}