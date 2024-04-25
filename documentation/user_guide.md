# User Guide

## Installation

1. Download dependancies with:
```
poetry install
```
2. Start the program with the command:
```
poetry run invoke start
```
## How to use the software / play the game

The program is a game of connect 4, where the goal is to get 4 of your pieces in a row, horizontally, vertically, or diagonally. The game features 7 columns where the player can put their piece, where the piece will then fall to the bottom.

The game runs in turns, with one player putting their piece on the board and then the other player putting their piece next. If the entire board is filled with no winner, the game ends in a tie.

The game runs on the command terminal. When it is your turn the game will ask you to choose the column you want to put your piece in. If your input is invalid, you will be asked to input your move again.

If you want to quit the game, press q when it is your turn.

## Commandline

#### Run the program
You can run the program with the command:
```
poetry run invoke start
```
#### Testing
You can run tests on the program with:
```
poetry run invoke test
```
#### Test coverage
You can generate the test coverage with:
```
poetry run invoke coverage-report
```
#### Pylint
You can check the requirements outlined in the .pylintrc file with:
```
poetry run invoke lint
```
