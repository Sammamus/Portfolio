package main

import "fmt"

type contactInfo struct {
	email   string
	zipCode int
}

type person struct {
	firstName string
	lastName  string
	contact   contactInfo
}

func main() {
	// alex := person{"Alex", "Anderson"}
	// alex := person{firstName: "Alex", lastName: "Anderson"}

	// var alex person

	// alex.firstName = "Alex"
	// alex.lastName = "Anderson"

	// ash := person{
	// 	firstName: "Ash",
	// 	lastName: "Harper",
	// 	contact: contactInfo{
	// 		email: "ash.harper1@icloud.com",
	// 		zipCode: 78641,
	// 	},
	// }

	var ash person

	ash.firstName = "Ash"
	ash.lastName = "Harper"
	ash.contact.email = "ash.harper1@icloud.com"
	ash.contact.zipCode = 78641

	// fmt.Println(ash)

	ash.print()
	ash.updateName("Asheron")

	ash.print()

}

func (pointerToPerson *person) updateName(newFirstName string) {
	(*pointerToPerson).firstName = newFirstName
}

func (p person) print() {
	fmt.Printf("%+v", p)
}
