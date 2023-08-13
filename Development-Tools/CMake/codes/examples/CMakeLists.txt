# Do not run cmake with this file
# As there are no source codes in the directory

# CMake minimum version
cmake_minimum_required(VERSION 3.10)

# Project name
project(CMakeExample)

# Store source code folder in a variable
aux_source_directory(./src SRC_DIR)

# include a directory during compilation, like header files
include_directories(./headers)

# Specify build target
add_executable(CMakeExample ${SRC_DIR})