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
    # TODO: finish this function!
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves)


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
    raise NotImplementedError


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
    raise NotImplementedError


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
            print("Simulated score of %f returned" % simulated_score)
            print("Simulated state: ")
            print(simulated_state);
            if(simulated_score > max_a) :
                max_a = simulated_score
                best_move = move
                self.best_move = best_move

        print("Best found move has score %f",max_a)
        print("Best move is")
        print(best_move)
        return best_move

    def result(self, game_state, a):
        #print("result, Time left is: %f" % self.agent.time_left())
        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            print("Time left is: %f" % self.agent.time_left())
            raise SearchTimeout()
        return game_state.forecast_move(a)

    def max_value(self, game_state, remaining_depth):
        print("max_value, Time left is: %f, remaining depth %d" % (self.agent.time_left(), remaining_depth))
        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            raise SearchTimeout()

        print("max_value legal moves len %d" % len(game_state.get_legal_moves()))

        if remaining_depth == 0:
            current_score = self.score_fn(game_state,self.agent)
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
        print("min_value, Time left is: %f, remaining depth %d" % (self.agent.time_left(), remaining_depth))
        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            raise SearchTimeout()

        if remaining_depth == 0:
            current_score = self.score_fn(game_state,self.agent)
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
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout as st:
            return best_move  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
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


class AlphaBetaHelper :

    def __init__(self, agent, game, depth, score_fn, alpha, beta):
        self.agent = agent
        self.game = game
        self.best_move = None
        self.depth = depth
        self.score_fn = score_fn
        self.alpha = alpha
        self.beta = beta
        self.actions = {}

        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            raise SearchTimeout()

    def decision(self):
        #print("decision, Time left is: %f" % self.agent.time_left())
        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            raise SearchTimeout()

        v = self.max_value(self.game,self.depth, self.alpha,self.beta)

        if(v == float("-inf") or v == float("inf")) :
            best_move = (-1,-1)
        else :
            best_move = self.actions[v]
        print("Returning move: "+str(best_move[0])+" , "+str(best_move[1])+" with score: "+str(v))
        return best_move

    def result(self, game_state, a):
        #print("result, Time left is: %f" % self.agent.time_left())
        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            print("Time left is: %f" % self.agent.time_left())
            raise SearchTimeout()
        return game_state.forecast_move(a)

    def max_value(self, game_state, depth, alpha, beta):
        print("max_value, Time left is: %f" % (self.agent.time_left()))
        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            raise SearchTimeout()

        print("max_value legal moves len %d" % len(game_state.get_legal_moves()))

        if depth == 0 or len(self.game.get_legal_moves()) == 0:
            current_score = self.score_fn(game_state,self.agent)
            print("max_value depth 0, returning score of %f" % current_score)
            return current_score

        v = float("-inf")

        for a in game_state.get_legal_moves() :
            v = max(v, self.min_value(self.result(game_state,a),depth - 1, alpha,beta))
            self.actions[v] = a

            if v >= beta :
                return v
            alpha = max(alpha,v)

        return v

    def min_value(self, game_state, depth, alpha, beta):
        print("min_value, Time left is: %f" % (self.agent.time_left()))
        if self.agent.time_left() < self.agent.TIMER_THRESHOLD:
            raise SearchTimeout(self.best_move)

        if depth == 0 or len(self.game.get_legal_moves()) == 0:
            current_score = self.score_fn(game_state,self.agent)
            print("min_value depth 0, returning score of %f" % current_score)
            return current_score

        v = float("inf")

        for a in game_state.get_legal_moves() :
            v = min(v, self.max_value(self.result(game_state,a),depth - 1, alpha,beta))
            self.actions[v] = a

            if v <= alpha :
                return v
            beta = min(beta,v)

        return v


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
        best_move = (-1, -1)

        search_depth = 1

        while self.time_left() > self.TIMER_THRESHOLD:

            try:
                # The try/except block will automatically catch the exception
                # raised when the timer is about to expire.
                best_move = self.alphabeta(game,search_depth)

            except SearchTimeout as st:
                return best_move  # Handle any actions required after timeout as needed

            search_depth = search_depth + 1

        # Return the best move from the last completed search iteration
        return best_move

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
            raise SearchTimeout()


        # TODO: finish this function!

        abh = AlphaBetaHelper(self, game, depth, self.score, alpha, beta)
        best_move = abh.decision()

        return best_move
