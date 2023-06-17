# ChessAi Introduction
K16 (Kyro 16) is a chess minimax algorithm that uses a range of functions to determine what and where it moves with a **main** depth of ~3 (moves ahead) midgame. The depth will increase depending on the game status (n pieces on the board)

# Advantages

- Endgames evaluation works better; checkmates with KQk is now inevitable. Other states such as KRk and KBBk checkmates **can** be found, however may do a indirect path towards checkmate
- K16 Engine can play as white or black
- Opening moves are intergrated, so computing values at the start is not needed (instant play for first moves)

# Disadvantages

- Project still in development, expect some logic issues in the K16 Engine play.
- This project is regularly updated locally on my pc, updates here will be a finalized version.
- Endgames are more accurate at the cost of a higher depth, meaning higher computing time.
- The bot assumes it has infinite time limit, I will not be working on any time constraint.
- Written in Python and not C++, which is generally a lot slower, and a large decrease in depth (to ~3 midgame)

# Additions

- Engine types: 1 and 2. 1 is faster, and 2 is slower but (?) more accurate
- Evaluation methods improved such as endgame piece tables and increased depth
- WIP chess bot - the moves are based on its own evaluation of position methods and may not represent the 'best' moves possible, such as stockfish

# Things I need to add
- Increased depth if low legal moves available
- Increase the values of piece mappings so it can decide if taking is really the best option and not doing an improving / repositional move
- calculate a supposed infinite number of takes until there is no takes left, then record the material value and add it on
- Saved memory (transposition table) in depth_handler.py

# Unfamiliar with SAN Notation?
- Check out this link: https://support.chess.com/article/409-what-do-the-numbers-and-letters-like-knight-c-3-mean
