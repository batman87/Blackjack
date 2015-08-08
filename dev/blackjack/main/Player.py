__author__ = 'devadasmallya'

from Contestant import *


class Player(Contestant):
    def __init__(self):
        Contestant.__init__(self)
        # Betting related info
        self.cash_amount = 0  # Total amount of cash a player has
        self.bet = 0  # Amount bet in current round
        self.insurance = False  # Insurance for Blackjack
        self.split = False  # Split ?
        self.double_down = False  # Double Down ?
