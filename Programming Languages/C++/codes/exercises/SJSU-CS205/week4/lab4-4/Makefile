SRC_DIR = ./src
SOURCE  = $(wildcard $(SRC_DIR)/*.cpp)
OBJS    = $(patsubst %.cpp, %.o, $(SOURCE))
TARGET  = main
INCLUDE = -I./headers

# Options to compiler
CC      = g++
CFLAGS  = -c -Wall $(INCLUDE)

$(TARGET):$(OBJS)
	$(CC) -o $@ $(OBJS)
%.o: %.cpp
	$(CC) $(CFLAGS) $< -o $@

post_compile:
	rm -f $(SRC_DIR)/*.o

clean:
	rm -f $(SRC_DIR)/*.o
	rm -f $(TARGET)

.PHONY: post_compile clean

compile: $(TARGET) post_compile
	@:

.DEFAULT_GOAL := compile