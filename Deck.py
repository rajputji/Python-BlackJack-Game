"""
AUTHOR

    Abhishek Rajput <Abhishekrajput676@gmail.com>

This module Creates a Deck of 52 card well shuffled using the library function 'shuffle' from 'random' library.

"""

from random import shuffle

def createDeck():
    Deck = []
    faceValues=["A","J","Q","K"]
    for _ in range(4):
        for card in range(2,11):
            Deck.append(str(card))
        for card in faceValues:
            Deck.append(card)
    shuffle(Deck)
    return Deck