import cProfile
import chess
from time import time
from depth_handler import set_depth, optimal_move
from evaluation import check_end_game

board = chess.Board()

ENGINE = "K16_2"  # Kyro16
MAX_DEPTH = None  # None = Automatic, would recommend keeping it that way

# K16_1 - Slower, lower depth search but supposedly more accurate
# K16_2 - Faster, higher depth search
# K16_BLEND - (NOT AVAILABLE) Complement of both engines merged into one (alternating switch)

TYPES = {"K16_1": 1, "K16_2": 2, "K16_BLEND": 3}

if ENGINE in TYPES:
    TYPE = TYPES[ENGINE]


def play():
    global MAX_DEPTH
    print(board)

    while not board.is_game_over() or board.is_stalemate() or board.is_repetition():
        print("Board with fen: ", board.fen())
        if board.turn == chess.WHITE:
            start = time()

            MAX_DEPTH = set_depth(board, engineType=TYPE) if MAX_DEPTH is None else MAX_DEPTH
            best_move, evaluation = optimal_move(MAX_DEPTH, board, engineType=TYPE, end_game=check_end_game(board), debug=True)
            board.push(best_move)
            print("\n")
            print(f"Bot has played {best_move} with an evaluation of {evaluation} in {-(start - time())}s")
            print(board)
        else:
            board.push_san(input("Your move: "))
            print(board)
            print(f"{ENGINE} Engine is thinking...")


# cProfile.run("play()")  # debug purposes after run

play()

print(board.result())
