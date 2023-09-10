import cProfile
import chess.pgn
import multiprocessing as mp

from depth_handler import set_depth, optimal_move
from evaluation import is_end_game, evaluate
from opening_handler import *
from time import time

# FOREWORD: Make sure to calculate material advantage after takes n (inf) times to make it not think its a good trade at depth of 4

ENGINE = "K16_2"  # Engine model
COMPUTER = chess.WHITE  # Which side the computer plays as

# Just realized it loops through all squares after each move push and calculating free files may be unnecessary as
# the move pushed doesn't open the file, it assumes a blind new evaluation after each push. This is an efficiency
# issue I cannot be bothered to address yet.

# K16_1 - Slower, lower depth search but supposedly more accurate
# K16_2 - Faster, higher depth search
# K16_BLEND - (NOT AVAILABLE) Complement of both engines merged into one (alternating switch)

# r5k1/1nqp1ppp/p1p1r3/1p2P3/4NBPb/1Q6/PPP2P1P/3RR1K1 w - - 4 20
# 8/8/8/3KR3/8/5k2/8/8 w - - 10 6
# r1bq1rk1/pppp1ppp/2n5/1B1P4/1b2p3/5N2/PPPPQPPP/R1B1K2R w KQ - 2 8
# 1k6/2n1q1pp/pp6/8/4r3/1P4Q1/P1P2PPP/5RK1 w - - 0 30

board = chess.Board("8/8/8/8/3k4/8/7K/7Q w - - 0 1")  # Initializes the chess board. You can set the board FEN position as a string in the brackets

MAX_DEPTH = 6  # None = Automatic, would recommend keeping it that way
DO_OPENING = False  # Should the computer play instant openings?
PROCESSORS = mp.cpu_count()  # Using all CPU's for faster (multi) processing - changing this to a value can cause results to vary

game = chess.pgn.Game()  # To show game moves at the end / when you stop the program
book = book_to_array()  # Used once to convert book.txt to a readable array (used for opening moves)

# print(evaluate(board, engineType=2))  # should be zero

if board.fen() != board.starting_fen: DO_OPENING = False


def K16_move():
    TYPES = {"K16_1": 1, "K16_2": 2, "K16_BLEND": 3}; TYPE = 2  # default type 2 (faster version)
    if ENGINE in TYPES: TYPE = TYPES[ENGINE]
    max_depth = set_depth(board, engineType=TYPE) if MAX_DEPTH is None else MAX_DEPTH
    start = time()
    best_move, evaluation = optimal_move(max_depth, board, engineType=TYPE, processes=PROCESSORS, end_game=is_end_game(board), debug=True)
    board.push(best_move)
    print(f"\nBot has played {best_move} with an evaluation of {evaluation / 100} in {round((time() - start), 3)} seconds\n")
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
            print(f"BASE EVALUATION: {evaluate(board, engineType=1) / 100}")
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

if __name__ == '__main__':
    mp.freeze_support()
    try:
        play()
        # cProfile.run("play()")  # debug purposes after run
    except KeyboardInterrupt:
        print(chess.pgn.Game.from_board(board))

print(board.result())

if board.is_game_over():
    print(chess.pgn.Game.from_board(board))
