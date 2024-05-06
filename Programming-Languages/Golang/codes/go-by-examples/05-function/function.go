package main

import "fmt"

func main() {
	basicFunctionExample()
	funcWithMultipleReturnExample()
	variadicFunctionExamples()
	closureExample()
	recursionExample()
}

// Add type after parameters, and add type of return value after parameters of function
func plusTwoNums(a int, b int) int {
	return a + b
}

// If multiple parameters have same type, then you can write type only after the last parameter that have same types
func plusThreeNums(a, b, c int) int {
	return a + b + c
}

func basicFunctionExample() {
	// Code examples of basic function
	fmt.Println("Return value of function", plusTwoNums(1, 2))

	// Call function by name(args)
	plusThreeNums(1, 2, 3)
	fmt.Println()
}

func returnTwoNums() (int, int) {
	return 3, 7
}

func funcWithMultipleReturnExample() {
	// Code examples of functions that have multiple return values
	// You can define a function that return multiple values, with parenthesis around returning types
	// When you call the function, you need to have the same amount of variables
	three, seven := returnTwoNums()
	fmt.Println("Function with multiple return values", three, seven)

	// If you only need a subset of returning values, you can use blank identifier
	_, num2 := returnTwoNums()
	fmt.Println("Function return with blank identifier", num2)
	fmt.Println()
}

func sum(nums ...int) int {
	fmt.Println("input parameter", nums)
	sum := 0
	for num := range nums {
		sum += num
	}
	return sum
}

func variadicFunctionExamples() {
	// Code example of variadic function
	// Variadic function is the function that has arbitrary number of parameters
	sum1 := sum(1, 2)
	fmt.Println("Sum of 1, 2", sum1)

	sum2 := sum(1, 2, 3)
	fmt.Println("Sum of 1, 2, 3", sum2)

	sum3 := sum(1, 2, 3, 4)
	fmt.Println("Sum of 1, 2, 3, 4", sum3)

	// You can pass all the numbers in a slice
	// Use ... after name of slice to pass all values in the slice
	s := []int{1, 2, 3, 4, 5}
	fmt.Println("Sum of s", sum(s...))
	fmt.Println()
}

func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func closureExample() {
	// Code examples of closure
	// A closure is a function that closes over a certain variables
	// So that user doesn't have access to this variable
	getNextInt := intSeq()

	fmt.Println("Value of i in closure", getNextInt())
	fmt.Println("Value of i in closure", getNextInt())
	fmt.Println("Value of i in closure", getNextInt())
	fmt.Println("Value of i in closure", getNextInt())
	fmt.Println("Value of i in closure", getNextInt())

	// State of each function is unique
	newInts := intSeq()
	fmt.Println("State of each function is unique", newInts())
	fmt.Println()
}

func fib(num int) int {
	if num < 2 {
		return 1
	} else {
		return fib(num-1) + fib(num-2)
	}
}

func recursionExample() {
	// Code example of recursion
	// Recursion is those functions that calls themselves within those functions
	val1 := fib(7)
	fmt.Println("7th number in Fibonacci sequence", val1)
	fmt.Println()
}
