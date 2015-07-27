__author__ = 'devadas'

from Cards import *

class Game:
    def __init__(self, num_decks):
        self.cards = Cards(num_decks)
        self.cards.shuffle()

    def reshuffle(self, num_decks):
        self.cards.shuffle()

    def deal(self):
        player_total = 0
        dealer_total = 0

        # Player turn
        c = self.cards.getCard()
        player_total = self.addTotal(player_total, c)
        print "P: ", c

        # Dealer turn
        c = self.cards.getCard()
        dealer_total = self.addTotal(dealer_total, c)
        print " D: ", c

        # Player turn
        c = self.cards.getCard()
        player_total = self.addTotal(player_total, c)
        print "P: ", c

        # Dealer Turn
        c = self.cards.getCard()
        dealer_total = self.addTotal(dealer_total, c)
        last_dealer_card = c
        print " D: X"

        player_hit = True

        while player_hit:
            choice = raw_input("Hit/Stay? [h/s]")
            if choice == 's':
                player_hit = False
            elif choice == 'h':
                c = self.cards.getCard()
                player_total = self.addTotal(player_total, c)
                print "P: ", c
                if(player_total > 21):
                    print "OOOOOHHHH BUST!!!"
                    return
            else:
                print "Invalid choice"

        print "\n"

        print "Dealer turn"

        print last_dealer_card

        dealer_total = self.dealerPlay(dealer_total)

        if dealer_total > 21:
            print "Dealer BUST!! YOU WIN!!"
            return

        print "Player total: ", player_total, " Dealer Total: ", dealer_total

        if dealer_total > player_total:
            print "Sorry dealer wins!"
        elif player_total > dealer_total:
            print "Congratulations! You win!"
        else:
            print "Draw"



    def hit(self):
        pass

    def dealerPlay(self, t):
        while t < 17:
            c = self.cards.getCard()
            t = self.addTotal(t, c)
            print c
        return t

    def faceCard(self, c):
        return c == 'J' or c == 'Q' or c == 'K' or c == 'A'

    def addTotal(self, t, c):
        if self.faceCard(c):
            if c == 'A':
                t += 11
            else:
                t += 10
        else:
            t += int(c)

        return t

game = Game(1)
game.deal()