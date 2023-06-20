package main

import "fmt"

// shapes
type triangle struct {
	b float64
	h float64
}
type square struct {
	sl float64
}

func (t triangle) getArea() float64 {
	return .5 * t.b * t.h
}

func (s square) getArea() float64 {
	return s.sl * s.sl
}

// interface
type shape interface {
	getArea() float64
}

func main() {

	sq := square{
		5.5,
	}

	tri := triangle{
		5.5,
		7.8,
	}

	printArea(sq)
	printArea(tri)

}

func printArea(s shape) {
	fmt.Println(s.getArea())
}
