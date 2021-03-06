"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class WrappedSearchTimeout(Exception) :

    def __init__(self, best_move):
        self.best_move = best_move

class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """

debug = False

def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # This is a linear combination of own moves and opponent availables moves,
    # which focuses more on limiting the opponents remaining moves than on increasing
    # the player's own moves due to the 1.5 penalty factor applied to opponent moves
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return own_moves - 1.5 * opp_moves


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!

    # This heuristic attempts to see how many moves a player has that
    # are near to the center of the board; the idea is to try to create
    # partitions

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = game.get_legal_moves(player)
    mid_width = float(game.width / 2)
    mid_height = float(game.height / 2)

    score = 0
    # Take sum of squared distance of move from midpoint
    for move in own_moves :
        score = score + (move[0] - mid_height)**2 + (move[1] - mid_width)**2

    # Invert the score; small squared distances is better
    score = 1 / max(score,100)

    return score

def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!

    # This score gives points for a position with many that are close to the position of the opposing
    # player, on the theory that they could help make a partition

    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = game.get_legal_moves(player)
    other_position = game.get_player_location(game.get_opponent(player))
    mid_width = float(game.width / 2)
    mid_height = float(game.height / 2)

    score = 0
    # Take sum of squared distance of move from midpoint
    for move in own_moves :
        score = score + (move[0] - other_position[0])**2 + (move[1] - other_position[1])**2

    # Invert the score; small squared distances is better
    score = 1 / max(score,100)

    return score


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxHelper :

    def __init__(self, agent, game, depth, score_fn):
        self.agent = agent
        self.game = game
        self.depth = depth
        self.best_move = None
        self.score_fn = score_fn
        #print("Time left is: %f" % self.agent.time_left())
        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            raise SearchTimeout()

    def decision(self):
        #print("decision, Time left is: %f" % self.agent.time_left())
        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            raise WrappedSearchTimeout(self.best_move)
        max_a = float("-inf")
        best_move = None

        if len(self.game.get_legal_moves()) == 0:
            return (-1,-1)

        for move in self.game.get_legal_moves() :
            simulated_state = self.game.forecast_move(move)
            if(self.depth and self.depth > 0) :
                simulated_score = self.min_value(simulated_state,self.depth - 1)
            else :
                simulated_score = self.min_value_it(simulated_state)
            if debug:
                print("Simulated score of %f returned" % simulated_score)
                print("Simulated state: ")
                print(simulated_state)
            if(simulated_score > max_a) :
                max_a = simulated_score
                best_move = move
                self.best_move = best_move

        if debug:
            print("Best found move has score %f",max_a)
            print("Best move is")
            print(best_move)
        return best_move

    def result(self, game_state, a):
        #print("result, Time left is: %f" % self.agent.time_left())
        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            if debug:
                print("Time left is: %f" % self.agent.time_left())
            raise SearchTimeout()
        return game_state.forecast_move(a)

    def max_value(self, game_state, remaining_depth):
        if debug:
            print("max_value, Time left is: %f, remaining depth %d" % (self.agent.time_left(), remaining_depth))
        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            if debug:
                print("Raising search timeout")
            raise SearchTimeout()

        if debug:
            print("max_value legal moves len %d" % len(game_state.get_legal_moves()))

        if remaining_depth == 0:
            current_score = self.score_fn(game_state,self.agent)
            if debug:
                print("returning score of %f" % current_score)
            return current_score

        else :
            v = float("-inf")

            if len(self.game.get_legal_moves()) == 0:
                return (-1,-1)

            for a in game_state.get_legal_moves() :
                if remaining_depth > 0 :
                    v = max(v, self.min_value(self.result(game_state,a), remaining_depth - 1))
            return v

    def min_value(self, game_state, remaining_depth):
        if debug :
            print("min_value, Time left is: %f, remaining depth %d" % (self.agent.time_left(), remaining_depth))
        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            if debug:
                print("Raising search timeout")
            raise SearchTimeout()

        if remaining_depth == 0:
            current_score = self.score_fn(game_state,self.agent)
            if debug:
                print("returning score of %f" % current_score)
            return current_score
        else :
            v = float("inf")
            if len(self.game.get_legal_moves()) == 0:
                return (-1,-1)
            for a in game_state.get_legal_moves() :
                if remaining_depth > 0 :
                    v = min(v, self.max_value(self.result(game_state,a),remaining_depth - 1))
            return v

class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = None
        if len(game.get_legal_moves()) == 0 :
            best_move = (-1,-1)
        else :
            best_move = game.get_legal_moves()[0]

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            best_move = self.minimax(game, self.search_depth)
            if debug :
                print("Returning: %d,%d" % (best_move[0], best_move[1]))
            return best_move

        except SearchTimeout as st:
            if debug :
                print("Caught search timeout")
                print("Returning: %d,%d" % (best_move[0], best_move[1]))
            return best_move  # Handle any actions required after timeout as needed


        # Return the best move from the last completed search iteration
        if debug:
            print("Returning: %d,%d" % (best_move[0], best_move[1]))
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        # print("Time left is: %f" % self.time_left())
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!

        mh = MinimaxHelper(self, game, depth, self.score)
        best_move = mh.decision()

        return best_move


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # TODO: finish this function!
        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout

        if debug :
            print("Starting state")
            print(game.to_string())

        best_move = (-1, -1)

        search_depth = 1

        while self.time_left() > self.TIMER_THRESHOLD:

            try:
                # The try/except block will automatically catch the exception
                # raised when the timer is about to expire.
                best_move = self.alphabeta(game,search_depth)
                if debug:
                    print("Best move found of: %d,%d" % (best_move[0],best_move[1]))

            except SearchTimeout as st:
                if debug:
                    print("Timeout, best move found of: %d,%d" % (best_move[0],best_move[1]))
                return best_move  # Handle any actions required after timeout as needed

            search_depth = search_depth + 1

        # Return the best move from the last completed search iteration
        if debug:
            print("Ran out of time")
        return best_move

    def max_value(self, game_state, depth, alpha, beta):
        if debug:
            print("max_value, depth %d, Time left is: %f" % (depth, self.time_left()))
        if self.time_left() < self.TIMER_THRESHOLD:
            if debug:
                print("Raising timeout")
            raise SearchTimeout()

        # print("max_value legal moves len %d" % len(game_state.get_legal_moves()))

        if len(game_state.get_legal_moves()) == 0 :

            if game_state.is_loser(self):
                return float("-inf")

            if game_state.is_winner(self):
                return float("inf")


        if depth == 0:
            current_score = self.score(game_state,self)
            if debug:
                print("Terminal state, max_value depth 0, returning score of %f" % current_score)
            return current_score

        v = float("-inf")

        for a in game_state.get_legal_moves() :
            v = max(v, self.min_value(game_state.forecast_move(a),depth - 1, alpha,beta))
            # print("v is %f, would set action to: %d,  %d" % (v, a[0],a[1]))

            if v >= beta :
                if debug:
                    print("v of %f greater than beta for move %d,%d" % (v,a[0],a[1]))
                return v
            alpha = max(alpha,v)

        return v

    def min_value(self, game_state, depth, alpha, beta):
        if debug:
            print("min_value, depth %d, Time left is: %f" % (depth, self.time_left()))
        if self.time_left() < self.TIMER_THRESHOLD:
            if debug:
                print("Raising timeout")
            raise SearchTimeout()

        if(len(game_state.get_legal_moves()) == 0) :
            if len(game_state.get_legal_moves()) == 0 :

                if game_state.is_loser(self):
                    return float("-inf")

                if game_state.is_winner(self):
                    return float("inf")

        if depth == 0:
            current_score = self.score(game_state,self)
            if debug:
                print("min_value depth 0, returning score of %f" % current_score)
            return current_score

        v = float("inf")

        for a in game_state.get_legal_moves() :
            v = min(v, self.max_value(game_state.forecast_move(a),depth - 1, alpha,beta))
            if debug:
                print("v is %f, setting action to: %d,  %d" % (v, a[0],a[1]))

            if v <= alpha :
                if debug:
                    print("v of %f less than alpha for move %d,%d" % (v,a[0],a[1]))
                return v
            beta = min(beta,v)

        return v


    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            if debug:
                print("SearchTimeout")
            raise SearchTimeout()


        # TODO: finish this function!
        if len(game.get_legal_moves()) == 0 :
            if debug:
                print("No more legal moves")
            return (-1,-1)

        best_move = (12,12)
        best_move_score = float("-inf")

        for move in game.get_legal_moves() :
            move_score = self.min_value(game.forecast_move(move),depth - 1, alpha, beta)
            alpha = max(alpha, move_score)
            if move_score >= best_move_score :
                best_move_score = move_score
                best_move = move
        return best_move
