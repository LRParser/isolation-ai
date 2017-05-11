"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
from game_agent import MinimaxPlayer
from sample_players import GreedyPlayer

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        self.random_player = GreedyPlayer()
        self.minimax_player = MinimaxPlayer(search_depth=3)
        self.game = isolation.Board(self.random_player, self.minimax_player)

    def test_player(self):
        self.setUp()
        time_millis = lambda: 1000
        move = self.minimax_player.get_move(self.game,time_left=time_millis)
        print(move)

    def test_minimax(self):
        self.setUp()
        self.game.play()


if __name__ == '__main__':
    unittest.main()
