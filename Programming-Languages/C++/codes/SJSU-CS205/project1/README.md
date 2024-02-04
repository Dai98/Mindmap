### Project 1 - Calculator

Project 1 is to implement C-style calculator in command line. My goal is to practice a few utility functions for manipulating string functions like atoi or strip to practice C/C++ features like pointers and memory manipulation. I will avoid using any functions from <string.h> and implement on my own.

Also, this project follows [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html) to practice coding practice in C++.

The implemented functions are:
* str_util.h
    - str_len - strlen function from <string.h>
    - memory_move - memmove function from <string.h>
    - strip - a function that removes spaces(including \n and \t) at the beginning and end of the string. Like strip method in Python or trim method in Java.
    - str_equal - strcmp function from <string.h> 