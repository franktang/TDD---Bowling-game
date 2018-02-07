import unittest
from src.Game import Game


class test_game(unittest.TestCase):

    def test_sample(self):
        self.assertTrue(True)

    def test_noraml_game(self):
        game = Game("12345123451234512345")

        self.assertEqual(60, game.get_score())
