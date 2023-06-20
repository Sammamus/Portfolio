package main

import "fmt"

func main() {

	var a [11]int

	for i := range a {

		if i%2 == 0 {
			fmt.Println("Even:", i)
		} else {
			fmt.Println("Odd:", i)
		}
	}
}
