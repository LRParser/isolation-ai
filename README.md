# Isolation AI

This is an implementation of minimax search with iterative deepening and alpha-beta pruning.

It is designed to create an agent that performs well in a search space (9x9 isolation board) that cannot be exhaustively searched

Every time a square is occupied it is removed from play.

Agents move in rook-like patterns; the goal is to be the last agent which is not 'boxed in' or isolated (that is, which has additional squares it can move to)