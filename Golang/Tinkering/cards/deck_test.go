package main

import (
	"os"
	"testing"
)

func TestNewDeck(t *testing.T) {
	d := newDeck()

	expectedDeckLength := 16

	if len(d) != expectedDeckLength {
		t.Errorf("Expected deck length of %d, but got %d", expectedDeckLength, len(d))
	}

	if d[0] != "Ace of Spades" {
		t.Errorf("Expected first card of Ace of Spades, but got %v", d[0])
	}

	if d[len(d)-1] != "Four of Clubs" {
		t.Errorf("Expected last card of Four of Clubs, but got %v", d[len(d)-1])
	}
}

func TestSaveToDeckAndNewDeckFromFile(t *testing.T) {
	testFileName := "_decktesting"
	expectedDeckLength := 16

	os.Remove(testFileName)

	d := newDeck()
	d.saveToFile(testFileName)

	loadedDeck := newDeckFromFile(testFileName)

	if len(loadedDeck) != expectedDeckLength {
		t.Errorf("Expected deck length of %d, but got %d", expectedDeckLength, len(loadedDeck))
	}

	if loadedDeck[0] != "Ace of Spades" {
		t.Errorf("Expected first card of Ace of Spades, but got %v", loadedDeck[0])
	}

	if loadedDeck[len(loadedDeck)-1] != "Four of Clubs" {
		t.Errorf("Expected last card of Four of Clubs, but got %v", loadedDeck[len(loadedDeck)-1])
	}

	os.Remove(testFileName)

}
