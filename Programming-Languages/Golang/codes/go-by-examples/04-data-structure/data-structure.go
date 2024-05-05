package main

import (
	"fmt"
	"maps"
	"slices"
)

func main() {
	arrayExamples()
	sliceExample()
	mapExample()
	rangeExample()
}

func arrayExamples() {
	// Code example of array
	// Declare an array
	var a [5]int
	fmt.Println(a)

	// Change value of an element
	a[4] = 100

	fmt.Println(a)
	// Access an element
	fmt.Println(a[4])
	// Get length of an array
	fmt.Println(len(a))

	// Array with initialization
	b := [5]int{1, 2, 3, 4, 5}
	var c [5]int = [5]int{1, 2, 3, 4, 5}
	fmt.Println("Array with initialization", b)
	fmt.Println("Array with initialization", c)

	// Two dimensional array
	var d [2][3]int
	for i := range 2 {
		for j := range 3 {
			d[i][j] = i + j
		}
	}
	fmt.Println("Two dimensional array", d)

	fmt.Println()
}

func sliceExample() {
	// Code examples of slices
	var s []string
	// Uninitialized slice is equal to nil and has length of 0
	fmt.Println("Uninitialized slice", s, s == nil, len(s) == 0)

	// Use make to create empty slices with non-zero length
	s = make([]string, 3)
	// Use cap function to get capacity of slice
	fmt.Println("Empty non zero-length slice", s, s == nil, len(s), cap(s))

	// Set
	s[0] = "a"
	s[1] = "b"
	s[2] = "c"

	// Get
	fmt.Println("Retrieve an element from slice", s[2])

	// Slice can become larger than its initial capacity
	// Use builtin append function
	s = append(s, "e", "f")
	fmt.Println("Slice grows larger", s)

	// Slice can be copied
	var c = make([]string, len(s))
	copy(c, s)
	fmt.Println("Copy a slice from slice s", c)
	// c and s have different address
	fmt.Println("Copied slices have different addresses", &s[0], &c[0])

	// Slices also support slicing operation to take a range of elements like Python lists
	// Start indexes is included, but ending index is excluded
	fmt.Println("Take elements on index 2,3,4", s[2:5])

	// Declare and initialize a slice in one line
	s1 := []string{"x", "y", "z"}
	s2 := []string{"x", "y", "z"}

	// Check if two slices have same length and identical elements
	fmt.Println("If s1 and s2 have same elements", slices.Equal(s1, s2))

	// Two dimensional slices
	// Inner slices don't need to have same length
	var d = make([][]int, 3)
	for i := 0; i < 3; i++ {
		var inner = make([]int, i+1)
		for j := 0; j < i+1; j++ {
			inner[j] = i + j
		}
		d[i] = inner
	}
	fmt.Println("2 dimensional slices", d)

	fmt.Println()
}

func mapExample() {
	// Code example of Maps
	// Maps are hash map implementation in Golang, like map or dict in other languages
	// Initialize a map with string key and int values
	m := make(map[string]int)
	// Set values in map
	m["a"] = 1
	m["b"] = 2
	m["c"] = 3
	fmt.Println("Map", m)

	// Get values from map
	v1 := m["a"]
	v3 := m["c"]
	fmt.Println("Values from map", v1, v3)

	// Get the number of key-value pairs
	fmt.Println("Get number of key-value pairs", len(m))

	// Remove a key-value pair from map
	delete(m, "b")
	fmt.Println("Remove one key-value pair from map", m)

	clear(m)
	fmt.Println("Clear all key-value pairs from map", m)

	// There is an optional return value when retrieving a value from map
	// Whether does the corresponding key exists in this map
	value, valueExists := m["notExistingKey"]
	fmt.Println("Retrieving with a not existing key", value, valueExists)

	// Declare and initialize map in one line
	n1 := map[string]int{"x": 10, "y": 20, "z": 30}
	n2 := map[string]int{"x": 10, "y": 20, "z": 30}

	// Check if two maps have same key-value pairs
	fmt.Println("Check if two maps have same key-value pairs", maps.Equal(n1, n2))
	fmt.Println()
}

func rangeExample() {
	// Code examples of range
	// range is the iterator of data structures
	nums := []int{1, 2, 3, 4}
	sum := 0
	// Iterate through a slice with index
	for index, num := range nums {
		sum += num
		if index == 2 {
			fmt.Println("Element on index 2:", num)
		}
	}

	fmt.Println("Sum of the slice", sum)

	// range can also iterate through maps
	m := map[string]string{"a": "apple", "b": "banana"}
	// If receive two parameters, then both keys and values will be returned
	for key, value := range m {
		fmt.Printf("%s -> %s \n", key, value)
	}

	// If receive one parameter, then only keys will be returned
	for key := range m {
		fmt.Println("key is", key)
	}

	// String can also be iterated, runes will be returned
	for index, r := range "Golang" {
		fmt.Printf("Index %d -> Rune %d \n", index, r)
	}
	fmt.Println()
}
