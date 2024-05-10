# The Implementation Document

## The general structure of the program.

The general structure consists of four main parts:

- main.py that runs the game and both the players turn and AI's turn as well as updating the game state
- board.py that handles the board where the game is played on, any moves made onto that board as well as checking for a winner.
- player.py that handles the players inputs
- ai.py that handles the ai's inputs as well as the minimax-algorithm

## The time and space complexities

The code uses minimax algorithm, thus the Big O time for the code will always be O(m^d), where m is the number of possible moves and d is the maximum depth the algorithm goes. The code does employ alpha-beta pruning, iterative deepening, and a hash table, all to improve on the minimax algorithm. And in the best or avarage scenario it is far faster than the base minimax. Still they don't change the algorithm and there can be scenarios where the minimax cannot apply any of the improvements, thus the time complexity remains the same.
The space complexity for the algorithm is O(md) where m is the number of possible moves and d is the maximum depth the algorithm goes to. 

## Potential shortcomings and suggested improvements of the work.

- The user interface is currently text based. That could easily be switched to a more sophisticated user interface. 
- The code is currently set up as player vs AI, but the code could support player vs player or AI vs AI modes. This could be implemented to allow for different versions of the game.
- Currently the player always starts first. This does give the player a small advantage, but considering how difficult it is to win against the AI its fine. But the code could be set up to randomize the starting player.

## Use of extensive language models 

I have used gihub copilot to help write the code faster as well as copy sections that I have already written.

## References

References used in making this game.

https://en.wikipedia.org/wiki/Minimax

https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

https://www.neverstopbuilding.com/blog/minimax

https://en.wikipedia.org/wiki/Space_complexity

https://en.wikipedia.org/wiki/Time_complexity

