import cProfile
import chess
from time import time
from depth_handler import set_depth, optimal_move
from evaluation import check_end_game
import multiprocessing as mp

board = chess.Board()  # "3k4/7R/p2N1p2/8/8/8/PPP2PPP/2K4R b - - 0 27"

ENGINE = "K16_2"  # Engine model - leave blank for default engine (2) or write "K16_2"
MAX_DEPTH = None  # None = Automatic, would recommend keeping it that way
COMPUTER = chess.WHITE  # What colour the computer plays as
PROCESSORS = mp.cpu_count()  # Using all CPU's for faster (multi) processing - you can set it manually if you wish

# K16_1 - Slower, lower depth search but supposedly more accurate
# K16_2 - Faster, higher depth search
# K16_BLEND - (NOT AVAILABLE) Complement of both engines merged into one (alternating switch)


def K16_move():
    global MAX_DEPTH
    TYPES = {"K16_1": 1, "K16_2": 2, "K16_BLEND": 3}; TYPE = 2  # default type 2 (faster version)
    start = time()
    if ENGINE in TYPES: TYPE = TYPES[ENGINE]
    MAX_DEPTH = set_depth(board, engineType=TYPE) if MAX_DEPTH is None else MAX_DEPTH
    best_move, evaluation = optimal_move(MAX_DEPTH, board, engineType=TYPE, end_game=check_end_game(board), processes=PROCESSORS, debug=True)
    board.push(best_move)
    print(f"\nBot has played {best_move} with an evaluation of {evaluation} in {round(-(start - time()), 3)} seconds\n")
    print(board)
    return best_move, evaluation


def player_move(): board.push_san(input("Your move: ")); print(board); print(f"{ENGINE} Engine is thinking...")


def play():
    print(board)
    while not (board.is_game_over() or board.is_stalemate() or board.is_repetition()):
        print("Board with fen: ", board.fen())
        if board.turn != COMPUTER:
            K16_move()
        else:
            K16_move()


# cProfile.run("play()")  # debug purposes after run

if __name__ == '__main__':
    mp.freeze_support()
    play()

print(board.result())
