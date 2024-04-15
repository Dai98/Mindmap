package main

import (
	"fmt"
	"time"
)

func main() {
	ifElseExample()
	forLoopExample()
	switchCaseExample()
}

func ifElseExample() {
	// Code example of if-else branch
	var a = 7
	if a%2 == 0 {
		fmt.Println("7 is even")
	} else {
		fmt.Println("7 is odd")
	}

	if num := 9; num < 0 {
		fmt.Println("9 is negative")
	} else if num < 10 {
		fmt.Println("9 has 1 digit")
	} else {
		fmt.Println("9 has multiple numbers")
	}
	fmt.Println()
}

func forLoopExample() {
	// Code example of for loop

	// Traditional while loop
	i := 0
	for i <= 3 {
		fmt.Println("Traditional while loop", i)
		i++
	}

	// Traditional for loop
	for i := 0; i <= 3; i++ {
		fmt.Println("Traditional for loop", i)
	}

	// for range loop
	// range keyword won't reach the actual number
	for i := range 3 {
		fmt.Println("For loop with range", i)
	}

	// for loop without condition
	a := 0
	for {
		if a == 3 {
			break
		} else {
			fmt.Println("For loop without condition", a)
			a++
		}
	}

	// continue keyword
	for b := range 6 {
		if b%2 == 0 {
			continue
		} else {
			fmt.Println("Example with continue", b)
		}
	}
	fmt.Println()
}

func switchCaseExample() {
	// Code example of switch-case

	// Switch-case
	i := 2
	switch i {
	case 1:
		fmt.Println(i, "One")
	case 2:
		fmt.Println(i, "Two")
	case 3:
		fmt.Println(i, "Three")
	}

	// Expression in switch and default keyword
	switch time.Now().Weekday() {
	// cases with same action can put together with comma
	case time.Saturday, time.Sunday:
		fmt.Println("Today is weekend")
	// All other cases can be included as default
	default:
		fmt.Println("Today is weekday")
	}

	// Non-constants case condition expression
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Right now is before noon")
	default:
		fmt.Println("Right now is after noon")
	}

	// Use switch-case to determine value type
	valueType := func(i interface{}) {
		switch t := i.(type) {
		case int:
			fmt.Println(i, "int type")
		case bool:
			fmt.Println(i, "bool type")
		case string:
			fmt.Println(i, "string type")
		default:
			fmt.Printf("Don't know what type %T\n", t)
		}
	}

	valueType(10)
	valueType(true)
	valueType("Hello World!")
	valueType(10.0)
	fmt.Println()
}
