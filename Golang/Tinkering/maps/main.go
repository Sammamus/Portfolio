package main

import "fmt"

func main() {
	colors := map[string]string{
		"red":   "#ff0000",
		"green": "#4bf745",
		"white": "ffffff",
	}

	changeMap(colors)

	fmt.Println(colors)

	printMap(colors)

	// var colors map [string]string

	// colors := make(map[string]string)

	// colors["red"] = "#ff0000"
	// colors["green"] = "#4bf745"

	// fmt.Println(colors)
	// fmt.Println(colors["red"])

	// delete(colors, "green")
	// fmt.Println(colors)
}

func printMap(c map[string]string) {
	for color, hex := range c {
		fmt.Println("Hex code for is", hex)
	}
}

func changeMap(m map[string]string) {
	m["blue"] = "#238934"
}
