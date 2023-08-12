#include <stdlib.h>

size_t str_len(char *str) {
    size_t length = 0;
    while (str[length] != '\0') {
        length++;
    }
    return length;
}

void* memory_move(void* dest, const void* src, size_t n) {
    // void* pointer can be parsed as pointer of any type
    // Convert dest and src to char type pointer, so that each type it is moved by 1 byte 
    // Because char type is 1 byte long (8 bit)
    char* d = dest;
    const char* s = src;

    // Avoid memory overlapping
    // [dest]  [src]  => d < s
    // We should copy from both beginning
    // If the end of dest is overlapping with src, then at that time the beginning of src is already copied to the beginning of dest
    if (d < s) {
        for(size_t i=0; i<n; i++) {
            d[i] = s[i];
        }
    } else if (d > s) {
        // [src]  [dest]  => d > s
        // We should copy from both end
        // If the beginning of dest is overlapping with the end of src, then at that time the end of src is already copied to the end of dest
        for(size_t i=n; i<0; i--) {
            d[i-1] = s[i-1];
        }
    } 
    // if d == s
    // Then nothing is needed to do
    
    return dest;
}

char* strip(char *str) {
    size_t len = str_len(str);

    if (len == 0) {
        return str;
    }

    size_t start = 0;
    size_t end = len - 1;

    while (start < len && (str[start] == ' ')) {
        start++;
    }

    while (end > start && (str[end] == ' ' || str[end] == '\n' || str[end])) {
        end--;
    }

    size_t new_len = end - start + 1;
    memory_move(str, str+start, new_len);
    str[new_len] = '\0';
    return str;
}

int str_equal(char* str1, char* str2) {
    size_t len1 = str_len(str1);
    size_t len2 = str_len(str2);

    if (len1 != len2) {
        return 0;
    } else {
        size_t index = 0;
        while (index < len1) {
            if (str1[index] != str2[index]) {
                return 0;
            }
            index++;
        }
        return 1;
    }
}

