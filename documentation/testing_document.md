# The Testing Document

## The coverage report of the unit tests.

![Coverage report](https://github.com/Nanotiike/Harjoitustyo_connect4/blob/main/documentation/images/coverage.png)

## What has been tested and how?

Testing of the game functions in the board.py file:

- Printing of the board is succesful
- make_move function works correctly, both in success and failure
- undo_move works correctly
- check_for_winner correctly identifies if there is a winner
  - horizontally
  - vertically
  - diagonally

Testing of the player class:

- player choose_move works correclty in all scenarios
  - incorrect input
  - column full
  - quit
  - succesful move

Testing of the AI class and the minimax algorithm:

- minimax algorithm putputs the correct choice when:
  - winning is possible
  - enemy win in the next move
  - tie happens

## What kind of inputs were used for the testing?

Tests were done with inputs that vary from board states to different player inputs. Test inputs could be expanded, but the current ones cover majority of all the meaningful cases. 

## How can the tests be repeated?

Tests can be done using the following command:
```
poetry run invoke test
```
Test coverage can be recieved with the following command:
```
poetry run invoke coverage-report
```
