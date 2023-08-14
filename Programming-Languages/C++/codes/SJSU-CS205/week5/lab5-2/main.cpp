#include<stdio.h>

int main() {
    int a[]={2,4,6,8,10},y=1,*p;
    // p points to the second element in a array
    p=&a[1];
    // a points to the first element in the array
    printf("a = %p\np = %p\n",a, p);

    for(int i = 0; i < 3; i++) 
        y += *(p+i);
        // y = y (1) + 4 + 6 + 8 = 19
    printf("y = %d\n\n",y);

    int b[5]={1,2,3,4,5};
    // ptr points to the address after the whole array (or 6th element, if it were there)
    int *ptr=(int*)(&b+1);
    // b+4 is the fifth element in the array
    // ptr is 4 more bytes than the last element of the array
    // meaning that ptr is pointing to the memory space after b+4
    // Note that when we do add/substraction on pointers
    // It adds sizeof(int), not sizeof(int*)
    // Namely, b+1 is 4 more bytes of b, not 8 bytes (if your OS is 64-bit)
    printf("b = %p\nb+4 = %p\nptr = %p\n", b, b+4, ptr);
    // *(b+1) is the content of the second element, which is 2
    // ptr-1 moves back to the 5th element, which is 5
    // Note that b as a pointer points to the whole array
    // Even though you can use it as the pointer to the first element, 
    // it is not actually pointing to the first element
    printf("%d,%d\n", *(b+1), *(ptr-1));
    
    return 0;
}