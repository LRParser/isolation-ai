# Heuristic Analysis

## Introduction
I evaluated the performance of my agent using three custom-implemented evaluation functions. These were tested alongside a given 'improved_score' evaluation function which returned the difference between the number of moves available to the current player vs the number of moves available to the opponent.

These functions were implemented as follows: custom_score implemented a "Weighted Linear Combination" heuristic; custom_score_2 implemented a "Nearness to Center" heuristic; and custom_score_3 implemented a "Nearness to Opponent" heuristic 



For each of your three custom heuristic functions, evaluate the performance of the heuristic using the included tournament.py script. Then write up a brief summary of your results, describing the performance of the agent using the different heuristic functions verbally and using appropriate visualizations.