### CS 205 by SJSU

#### Code Structure
There are two general patterns for folders in this directory:
* week(n) - This is the code practice for content of week n
* project(n) - This is the n-th project of this course

I found out that the weekly practices also cover some valuable examples in C++ of knowledge beyond basic C++ syntax, including
* week1/exercise2 - Overflowing
* week2/exercise1 - Float comparison
* week2/lab2-1 - Two's Complement
* week4/lab4-2 - Little Endian & Big Endian

#### Environment & Version

Codes under this directory have following dependencies:

* [C++ Compiler - MinGW-w64 GCC](https://www.mingw-w64.org/)
* Makefile - GNU Make 4.4.1
* [CMake - 3.27.2](https://cmake.org/install/)

#### How to Run

If there are only header files (`*.h`) and C++ source codes (`*.cpp`) under a folder, use g++ to compile the codes, e.g.
```bash
# Step 1: Use g++ to compile
g++ main.cpp functions.cpp -o main

# Step 2: Run the executable
# Windows
./main.exe

# Linux
./main
```

If there is a `Makefile` file under a folder, use `make` to compile a project, e.g.
```bash
# Step 1: Use Makefile to compile
make

# Step 2: Run the executable
# Windows
./main.exe

# Linux
./main
```

If there is a `CMakeLists.txt` file under a folder, use `cmake` to compile a project, e.g.
```bash
# Step 1: Use cmake to generate Makefile
cmake .

# Step 2: Use Makefile to compile
make

# Step 3: Run the executable
# Windows
./main.exe

# Linux
./main
```
