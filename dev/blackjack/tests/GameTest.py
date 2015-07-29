__author__ = 'devadasmallya'

import unittest
from dev.blackjack.main.Game import Game


class GameTest(unittest.TestCase):
    def test_addTotal1(self):
        game = Game(1)
        cards = ['2', 'K']
        self.assertEqual(12, game.addTotal(cards))

    def test_addTotal2(self):
        game = Game(1)
        cards = ['2', 'A', 'K']
        self.assertEqual(13, game.addTotal(cards))

    def test_addTotal3(self):
        game = Game(1)
        cards = ['2', 'A', 'A', 'A', 'K', '6']
        self.assertEqual(21, game.addTotal(cards))

    def test_addTotal4(self):
        game = Game(1)
        cards = ['A', 'A', 'A', 'A']
        self.assertEqual(14, game.addTotal(cards))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GameTest)
    unittest.TextTestRunner(verbosity=5).run(suite)
