"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""
import timeit
import unittest

import isolation
from game_agent import MinimaxPlayer
from game_agent import AlphaBetaPlayer
from sample_players import GreedyPlayer

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        self.random_player = GreedyPlayer()
        self.minimax_player = MinimaxPlayer(search_depth=3)
        self.iterative_player = AlphaBetaPlayer(search_depth=6)
        self.game = isolation.Board(self.minimax_player, self.random_player)

    # def test_player(self):
    #     self.setUp()
    #     time_millis = lambda: 1000
    #     move = self.minimax_player.get_move(self.game,time_left=time_millis)
    #     print(move)
    #
    # def test_minimax(self):
    #     self.setUp()
    #     self.game.play()
    #
    # def test_iterative_deepening(self):
    #     self.setUp()
    #     self.iterative_player.time_left = lambda: 1000
    #     self.iterative_player.alphabeta(self.game,1)

    def test_alphabeta(self):
        self.setUp()
        self.game = isolation.Board(self.iterative_player, self.random_player,9,9)
        self.game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 50]
        self.game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 67, 47]
        print(self.game.to_string())

        time_left = lambda : 1000
        game_copy = self.game.copy()
        self.game.active_player.time_left = time_left
        print(self.game._active_player)
        next_move = self.game._active_player.alphabeta(game_copy, 2)
        print("Returning: %d,%d" % (next_move[0], next_move[1]))
        #self.game.play()




if __name__ == '__main__':
    unittest.main()
