import cProfile
import chess.pgn
import multiprocessing as mp

from time import time
from depth_handler import set_depth, optimal_move
from opening_handler import *

ENGINE = "K16_2"  # Engine model

# K16_1 - Slower, lower depth search but supposedly more accurate
# K16_2 - Faster, higher depth search
# K16_BLEND - (NOT AVAILABLE) Complement of both engines merged into one (alternating switch)

MAX_DEPTH = None  # None = Automatic, would recommend keeping it that way
DO_OPENING = True  # Should the computer play instant openings?
COMPUTER = chess.BLACK  # Which side the computer plays as
PROCESSORS = mp.cpu_count()  # Using all CPU's for faster (multi) processing - changing this to a value can cause results to vary

game = chess.pgn.Game()  # To show game moves at the end / when you stop the program
book = book_to_array()  # Used once to convert book.txt to a readable array (used for opening moves) 
board = chess.Board()  # Initializes the chess board. You can set the board FEN position as a string in the brackets


if board.fen() != board.starting_fen: DO_OPENING = False


def K16_move():
    TYPES = {"K16_1": 1, "K16_2": 2, "K16_BLEND": 3}; TYPE = 2  # default type 2 (faster version)
    if ENGINE in TYPES: TYPE = TYPES[ENGINE]
    max_depth = set_depth(board, engineType=TYPE) if MAX_DEPTH is None else MAX_DEPTH
    if len(list(board.legal_moves)) < 10: max_depth += 1
    start = time()
    best_move, evaluation = optimal_move(max_depth, board, engineType=TYPE, processes=PROCESSORS, debug=True)
    board.push(best_move)
    print(f"\nBot has played {best_move} with an evaluation of {evaluation / 100} in {round(-(start - time()), 3)} seconds\n")
    print(board)
    return best_move, evaluation


def player_move():
    while True:
        input_str = input("Your move: ")
        try:
            move = board.parse_san(input_str); board.push(move); break
        except ValueError:
            print("\nIllegal move. Try again.\n")
    print(board); print(f"{ENGINE} Engine is thinking...")


def computer_move():
    global count
    if DO_OPENING:
        count += 2

        game_line = get_MM(chess.pgn.Game.from_board(board))
        move = random_variation_move(book, game_line, count)

        if move is not None:
            board.push_san(move)
            print("\n")
            print(board)
        else:
            # print("====== END OF BOOK MOVES ======")
            K16_move()
    else:
        K16_move()


count = -2 if COMPUTER == chess.WHITE else -1


def play():
    print(board)
    while not (board.is_game_over() or board.is_stalemate() or board.is_repetition()):
        print("Board with fen: ", board.fen())
        if board.turn == COMPUTER:
            computer_move()
        else:
            player_move()


# cProfile.run("play()")  # debug purposes after run

if __name__ == '__main__':
    mp.freeze_support()
    try:
        play()
    except KeyboardInterrupt:
        print(chess.pgn.Game.from_board(board))

print(board.result())

if board.is_game_over():
    print(chess.pgn.Game.from_board(board))
