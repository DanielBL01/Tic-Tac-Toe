# Two Tic-Tac Toe games - Player vs Player and Player vs AI

The file 'player-player.py' is the standard player vs player game of tic-tac-toe
The file 'player-ai.py' is the player vs ai game of tic-tac-toe

Both games do not use any libraries or frameworks like Pygame. They just run on the terminal window

## Writing the AI

Tic-Tac-Toe is classified as a zero-sum game. Zero-sum is a situation in game theory in which one person's gain is equivalent to another's loss,

The Minimax algorithm is a solution of always minimizing the maximum possible loss which can result in a choice that a player can make.

This algorithm can be thought of like a backtracking recursion where at each node of the decision tree, the algorithm will look at each path to see which is the optimal path to minimize the maximum loss 

## Other games which use Minimax
Other common games that this algorithm is used for: Connect-4, Chess and Go (implementing Minimax for games like Chess and Go are obviously extremely difficult)
