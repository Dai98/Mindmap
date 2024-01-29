#include "stddef.h"
#ifndef STR_UTIL_H
#define STR_UTIL_H

size_t str_len(char *str);
char* strip(char *numString);
void* memory_move(void* dest, const void* src, size_t n);

#endif