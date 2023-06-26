package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
	"strings"
)

var started bool

func introduction() string {
	introduction := `Hello! This is Siri's Voice Box for your entertainment. 
	Wether it is for gags or annoying your significant other it's all fun under the sun.
	To start, after you activated my executable in your Mac Terminal, you just need to type the message and press enter.
	When you are done, just type 'q' and I will turn off.
	Thank you for choosing to spend your time with me.`

	return introduction
}

func response(input string) {

	switch {
	case strings.ToUpper(input) == "Q":
		exec.Command("say", "Goodbye").Output()
		os.Exit(0)
	default:
		exec.Command("say", input).Output()
	}
}

func main() {
	started = false
	scanner := bufio.NewScanner(os.Stdin)

	if !started {
		started = true
		fmt.Println(introduction())
		go response(introduction())
	}

	for scanner.Scan() {

		input := scanner.Text()

		input = strings.TrimSpace(input)
		go response(input)
	}
}
