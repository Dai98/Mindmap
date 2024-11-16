package main

import "fmt"

func main() {
	arrayExamples()
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
	fmt.Println()
}

func mapExample() {
	fmt.Println()
}

func rangeExample() {
	fmt.Println()
}
