# Heuristic Analysis

## Introduction
I evaluated the performance of my agent using three custom-implemented evaluation functions. These were tested alongside a given 'improved_score' evaluation function which returned the difference between the number of moves available to the current player vs the number of moves available to the opponent.

These functions were implemented as follows: custom_score implemented a "Weighted Linear Combination" heuristic; custom_score_2 implemented a "Nearness to Center" heuristic; and custom_score_3 implemented a "Nearness to Opponent" heuristic

## Overall Results of tournament.py

tournament.py returned each of the following results:

```                                           
                             Playing Matches                              
                        *************************                         

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3 
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost 
    1       Random       7  |   3     6  |   4     8  |   2     9  |   1  
    2       MM_Open      4  |   6     5  |   5     5  |   5     3  |   7  
    3      MM_Center     4  |   6     6  |   4     5  |   5     5  |   5  
    4     MM_Improved    4  |   6     5  |   5     4  |   6     1  |   9  
    5       AB_Open      7  |   3     3  |   7     6  |   4     6  |   4  
    6      AB_Center     4  |   6     6  |   4     2  |   8     4  |   6  
    7     AB_Improved    5  |   5     6  |   4     4  |   6     5  |   5  
--------------------------------------------------------------------------
           Win Rate:      50.0%        52.9%        48.6%        47.1%   
``` 


From this output, we consider the results of match #7, which was against the most sophisticated opponent. Here we can see that our custom_score or "Weighted Linear Combination" heuristic performed best, followed by custom_3, or "Nearness to Opponent", and then followed by custom_2, or "Nearness to Center"

## Summary of "Weighted Linear Combination" heuristic 

A visualization of the performance of this heuristic is given in the "Overall Results" above. It appears to have outperformed the "improved" heuristic because it gave a heigher weight to limiting the moves of the opponents vs keeping "own" moves count large. This may have incentivized the agent to find a partition earlier in the search, helping to explain its improved performance

## Summary of "Nearness to Center" heuristic

A visualization of the performance of this heuristic is given in the "Overall Results" table above. It appears to have underperformed the other heuristics. One possible reason for this could be that its not optimal to try to keep moves open in the center of the board if the opponent can't be fooled into creating a partition. This may explain why this heuristic (AB_Custom_2 in the table above) performed relatively well against a random agent but poorly against the "AB_Improved" agent.

## Summary of "Nearness to Opponent" heuristic

This heuristic rewarded an agent for placing himself nearer to the opponent. It is thought that this heuristic may have rewarded creating a partition, and it appears to have down so. However, without the intelligence of scoring the number of positions that remained available to the opponent after "moving towards" him, it merely drew a tie against the "AB_Improved" agent. It appears this heuristic may have similarity to the "improved" heuristic, seen by the lack of any meaningful improvement vs this heuristic.