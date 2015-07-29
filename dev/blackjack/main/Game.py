__author__ = 'devadas'

from Cards import *


class Game:
    def __init__(self, num_decks):
        self.cards = Cards(num_decks)
        self.cards.shuffle()

    def deal(self):
        new_game = True

        while new_game:
            if self.cards.isReshuffleReqd():
                print "Reshuffling cards.."
                self.cards.shuffle()

            player_cards = []
            dealer_cards = []
            player_bust = False
            dealer_bust = False
            player_blackjack = False

            # Player turn
            player_cards.append(self.getCard())
            self.addTotal(player_cards)
            print "Player: ", player_cards[0]

            # Dealer turn
            dealer_cards.append(self.getCard())
            self.addTotal(dealer_cards)
            print "    Dealer: ", dealer_cards[0]

            # Player turn
            player_cards.append(self.getCard())
            if self.isBlackjack(player_cards):
                print "BLACKJACK!!!!"
                player_blackjack = True
            else:
                player_total = self.addTotal(player_cards)
                print "Player: ", player_cards[1], "[", player_total, "]"

            # Dealer Turn
            dealer_cards.append(self.getCard())
            if player_blackjack:
                if self.isBlackjack(dealer_cards):
                    print "Dealer has Blackjack too. Draw."
                else:
                    print "Congratulations! You win!"

                new_game = self.checkNewGame()
                continue
            self.addTotal(dealer_cards)
            print "    Dealer: X"

            player_hit = True

            while player_hit and not player_bust:
                choice = raw_input("Hit/Stay? [h/s]")
                if choice == 's':
                    player_hit = False
                elif choice == 'h':
                    player_cards.append(self.getCard())
                    player_total = self.addTotal(player_cards)
                    print "Player: ", player_cards
                    if player_total > 21:
                        print "OOOOOHHHH BUST!!!"
                        player_bust = True
                else:
                    print "Invalid choice"

            if not player_bust:
                print "Dealer turn"

                print " Dealer: ", dealer_cards[1]

                dealer_total = self.dealerPlay(dealer_cards)

                if dealer_total > 21:
                    print "Dealer BUST!! YOU WIN!!"
                    dealer_bust = True

                if not dealer_bust:
                    print "Player total: ", player_total, " Dealer Total: ", dealer_total

                    if dealer_total > player_total:
                        print "Sorry dealer wins!"
                    elif player_total > dealer_total:
                        print "Congratulations! You win!"
                    else:
                        print "Draw"

            print "\n"
            print "*********"
            new_game = self.checkNewGame()

    def hit(self):
        pass

    def checkNewGame(self):

        while True:
            choice = raw_input("New game? [y/n]")

            if choice == 'y' or choice == 'Y':
                return True
            elif choice == 'n' or choice == 'N':
                return False
                break
            else:
                print "Invalid choice."

    def isBlackjack(self, cards):
        if not self.isFaceCard(cards[0]) or not self.isFaceCard(cards[1]):
            return False

        if cards[0] == 'A' or cards[1] == 'A':
            return True

        return False

    def getCard(self):
        return self.cards.getCard()

    def dealerPlay(self, cards):
        total = self.addTotal(cards)
        while total < 17:
            x = self.getCard()
            print x
            cards.append(x)
            total = self.addTotal(cards)

        return total

    def isFaceCard(self, c):
        return c == 'J' or c == 'Q' or c == 'K' or c == 'A'

    def addTotal(self, cards):
        max_total = 0
        min_total = 0

        for card in cards:
            if self.isFaceCard(card):
                if card == 'A':
                    if max_total + 11 > 21:
                        if min_total + 11 > 21:
                            max_total = min_total + 1
                        else:
                            max_total = min_total + 11
                    else:
                        max_total += 11
                    min_total += 1
                else:
                    if max_total + 10 > 21:
                        max_total = min_total + 10
                    else:
                        max_total += 10
                    min_total += 10
            else:
                max_total += int(card)
                min_total += int(card)

        return max_total


if __name__ == '__main__':
    game = Game(1)
    game.deal()
