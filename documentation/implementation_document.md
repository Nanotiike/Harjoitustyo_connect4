# The Implementation Document

## The general structure of the program.

The general structure consists of four main parts:

- main.py that runs the game and both the players turn and AI's turn as well as updating the game state
- board.py that handles the board where the game is played on, any moves made onto that board as well as checking for a winner.
- player.py that handles the players inputs
- ai.py that handles the ai's inputs as well as the minimax-algorithm

## The time and space complexities

Looking at the time and space complexities of the game, with n being the number of legal moves and m being the maximum depth of the tree:

- Space complexity: The game uses both minimax and alpha-beta pruning. The space complexity for minimax is O(nm). Alpha-beta pruning doesn't make this lesser in the worst case scenario, but in the best case scenario it would be O(n(m/2)).

- Time complexity: Similarly to space, time complexcity for minimax is O(n^m). With alpha-beta pruning the time complexity in the worst case is the same, but in the best case scenario, it is O(n^(m/2)).

## Potentially, performance and Big O analysis comparison

Big O analysis comparison for the game

## Potential shortcomings and suggested improvements of the work.

- The user interface is currently text based. That could easily be switched to a more sophisticated user interface. 
- The code is currently set up as player vs AI, but the code could support player vs player or AI vs AI modes. This could be implemented to allow for different versions of the game.

## Use of extensive language models 

I have used gihub copilot to help write the code faster as well as copy sections that I have already written.

## References

References used in making this game.

https://en.wikipedia.org/wiki/Minimax

https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

https://www.neverstopbuilding.com/blog/minimax

https://en.wikipedia.org/wiki/Space_complexity

https://en.wikipedia.org/wiki/Time_complexity

