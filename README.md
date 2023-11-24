# ChessAi Introduction
K16 (Kyro 16) is a chess engine that uses a range of algorithms and evaluation functions to determine which move is best, and this will run at a main depth of 3. The depth increase depending on the number of pieces on the board.

# Advantages

- Opening and endgame evaluations works better, forced checkmates are usually found
- K16 Engine can play as white or black
- Opening moves are intergrated, so computing values at the start is not needed (instant openings)

# Disadvantages

- K16 only evaluates what it considers 'best moves'
- Higher depth results in longer computing time.
- Midgame evaluations are usually more complicated, and accuracy may decrease

# Additions

- Engine types: K16_1 is slower but includes more evaluations, making it (?) more accurate, K16_2 is faster (higher depth) at the cost of (?) lower accuracy

# Things I need to add
- Increase the values of piece mappings so it can decide if taking is really the best option and not doing an improving / repositional move
- calculate a supposed infinite number of takes until there is no takes left, then record the material value and add it on

# Unfamiliar with SAN Notation?
- Check out this link: https://support.chess.com/article/409-what-do-the-numbers-and-letters-like-knight-c-3-mean
