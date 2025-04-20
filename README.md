# ChessAi Introduction
K16 - Kyro 16 is a chess engine that uses a range of algorithms and evaluation functions to determine and play which move is best.
This was for my A level Computer Science coursework (2024) and was my very first chess engine. Looking back at it, I knew very little!

# Requirements

- Python 3 or later
- python-chess module
- Knowledge of making moves with SAN notation (https://support.chess.com/article/409-what-do-the-numbers-and-letters-like-knight-c-3-mean)

# How to run

1. Make sure python-chess is installed by open your terminal and run the command `pip install python-chess`
2. Navigate to the directory through typing `cd .\ChessAi` in your terminal. 
3. Type `python K16_Engine.py` into the python terminal or run in a python IDE.

# Additional features

- To display the current PGN you can type `pgn`
- To display the current legal moves type `ls`
- Configurations are kept inside `K16_Engine.py` file such as depth search, allowing the use of book moves etc.. are safe to change if you wish.

