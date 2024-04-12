package main

import "fmt"

const global_constant = "Global Constant"

func main() {
	showValues()
	showVariables()
	showConstants()
}

func showValues() {
	// Values
	fmt.Println("Examples of values")
	// + can be used to concatenate strings
	fmt.Println("Go" + "lang")

	// + - * / % operator for integers and floats to do
	// addition, substraction, multiplication, division and modulus
	// two integers doing division will return an integer
	fmt.Println(3 + 5)
	fmt.Println(5 - 3)
	fmt.Println(2 * 6)
	fmt.Println(7 / 3)
	fmt.Println(7.0 / 3)
	fmt.Println(7 % 3)

	// logic operator && || ! for boolean value
	fmt.Println(true && false)
	fmt.Println(false || true)
	fmt.Println(!true)
	fmt.Println()
}

func showVariables() {
	// Variables
	fmt.Println("Example of Variables")
	// Use var to define a variable
	var a = "initial"
	fmt.Println(a)

	var b, c int = 10, 20
	fmt.Println(b, c)

	// Declared and uninitialized variables are zero-valued
	var d string
	fmt.Println("Zero valued string", d)

	var e int
	fmt.Println("Zero valued integer", e)

	var f bool
	fmt.Println("Zero valued bool", f)

	// := is a shorthand for declare and initializing a new variable
	g := "string value"
	fmt.Println(g)
	fmt.Println()
}

func showConstants() {
	// Constants
	fmt.Println("Example of Constants")
	// Use const to define a variable

	const a = 5
	fmt.Println(global_constant)
	fmt.Println(a)
}
