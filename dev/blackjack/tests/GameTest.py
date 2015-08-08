__author__ = 'devadasmallya'

import unittest
from dev.blackjack.main.Game import Game


class GameTest(unittest.TestCase):
    def test_addTotal1(self):
        game = Game(1)
        cards = ['2', 'K']
        self.assertEqual(12, game.add_total(cards))

    def test_addTotal2(self):
        game = Game(1)
        cards = ['2', 'A', 'K']
        self.assertEqual(13, game.add_total(cards))

    def test_addTotal3(self):
        game = Game(1)
        cards = ['2', 'A', 'A', 'A', 'K', '6']
        self.assertEqual(21, game.add_total(cards))

    def test_addTotal4(self):
        game = Game(1)
        cards = ['A', 'A', 'A', 'A']
        self.assertEqual(14, game.add_total(cards))

    def test_addTotal5(self):
        game = Game(1)
        cards = ['A', 'A', 'A', 'A', 'A', 'A', 'A']
        self.assertEqual(17, game.add_total(cards))

    def test_addTotal6(self):
        game = Game(1)
        cards = ['A', 'K', 'A', 'A', 'A', 'A', 'A', 'A']
        self.assertEqual(17, game.add_total(cards))

    def test_addTotal7(self):
        game = Game(1)
        cards = ['A', 'K', '3', 'A', 'A', 'A', 'A', 'A']
        self.assertEqual(19, game.add_total(cards))

    def test_getCard(self):
        game = Game(1)
        for i in range(20):
            print game.getCard(),


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GameTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
