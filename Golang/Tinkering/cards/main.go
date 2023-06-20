package main

func main() {
	// cards := newDeckFromFile("myCard")

	cards := newDeck()

	cards.shuffle()
	cards.print()

}
