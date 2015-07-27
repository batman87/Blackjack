__author__ = 'devadas'

import random

class Cards:
    def __init__(self, num_decks):
        self.decks = num_decks
        self.cards = [None] * 52 * num_decks
        self.itr = 0
        self.createDeck()

    def getNumberDecks(self):
        return self.decks

    def createDeck(self):
        x = 0

        # Add numbered cards
        for i in range(self.decks):
            for j in range(2, 11):
                for k in range(4):
                    self.cards[x] = str(j)
                    x += 1

        # Add Jack
        for i in range(self.decks):
            for j in range(4):
                self.cards[x] = "J"
                x += 1

        # Add Queen
        for i in range(self.decks):
            for j in range(4):
                self.cards[x] = "Q"
                x += 1

        # Add King
        for i in range(self.decks):
            for j in range(4):
                self.cards[x] = "K"
                x += 1

        # Add Ace
        for i in range(self.decks):
            for j in range(4):
                self.cards[x] = "A"
                x += 1

    def shuffle(self):
        random.shuffle(self.cards)

    def getCard(self):
        c = self.cards[self.itr]
        self.itr += 1
        return c

    def resetDeck(self):
        self.shuffle()
        self.itr = 0