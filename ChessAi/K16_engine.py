import cProfile
import chess.pgn
import multiprocessing as mp

from depth_handler import set_depth, optimal_move
from evaluation import is_end_game, evaluate
from opening_handler import *

from termcolor import colored
from time import time, sleep


# FOREWORD: Make sure to calculate material advantage after takes n (inf) times to make it not think it is a good trade at depth of 4

ENGINE = "K16_1"  # Engine model
MAX_DEPTH = None  # None = Automatic, would recommend keeping it that way
DO_OPENING = True  # Should the computer play instant openings?
MAX_BOOK_MOVES = 16  # if DO_OPENING is set to true, play x amount of book moves

DEBUG = True  # shows engine evaluation

board = chess.Board()  # Initializes the chess board. You can set the board FEN position as a string in the brackets

# K16_1 - Slower, lower depth search but supposedly more accurate
# K16_2 - Faster, higher depth search
# K16_BLEND - (NOT AVAILABLE) Complement of both engines merged into one (alternating switch)

# FEN positions below due to no quiescence search (it's too resource intensive to implement inb .py; it slows down the program)

# r5k1/1nqp1ppp/p1p1r3/1p2P3/4NBPb/1Q6/PPP2P1P/3RR1K1 w - - 4 20
# 8/8/8/3KR3/8/5k2/8/8 w - - 10 6
# r1bq1rk1/pppp1ppp/2n5/1B1P4/1b2p3/5N2/PPPPQPPP/R1B1K2R w KQ - 2 8
# 1k6/2n1q1pp/pp6/8/4r3/1P4Q1/P1P2PPP/5RK1 w - - 0 30
# r3r1k1/p1p2ppp/1pnq4/3p1b2/3Pn1P1/P2BBN2/2P2P1P/R3QRK1 b - g3 0 16
# r1bqk1nr/pppp1ppp/2n5/2b1p3/4P3/2N2N2/PPPP1PPP/R1BQKB1R w KQkq - 4 4
# r1b2rk1/p2p1ppp/1p5q/2p1p3/4Pb2/P1RP1P2/1P2BP1P/3Q2RK b - - 0 17
# 1rbq1rk1/pp2n1p1/3Np2p/5p2/3p3P/1Q4P1/P3PPB1/R1B2RK1 b - - 0 19
# r5k1/2p2pp1/1b5p/1P1P4/3QP1B1/5P1P/6P1/6K1 w - - 1 29 # WTF??
# rnbqkb1r/pppp1ppp/5n2/8/2P1p3/2N2N2/PP1PPPPP/R1BQKB1R w KQkq - 0 4  # RIP
# r1bqk1nr/ppp3pp/2n1pp2/3pP3/1b1P4/2N5/PPP1BPPP/R1BQK1NR w KQkq - 2 6


PROCESSORS = mp.cpu_count()  # Using all CPU's for faster (multi) processing - changing this to a value can cause results to vary

game = chess.pgn.Game()  # To show game moves at the end / when you stop the program
book = book_to_array(MAX_BOOK_MOVES)  # Used once to convert book.txt to a readable array (used for opening moves)

# print(evaluate(board, engineType=2))  # should be zero

if board.fen() != board.starting_fen: DO_OPENING = False


def symbolizeAndOutput(b):

    newBoard = b.unicode(invert_color=True).replace("⭘", "〇")
    for val in newBoard:
        if val not in [" ", "\n", "〇"]:
            if val in ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖", "♙"]:
                newBoard = newBoard.replace(val, f"\33[31m{val}\x1b[0m")
            else:
                newBoard = newBoard.replace(val, f"\33[34m{val}\x1b[0m")

            pass

    print(newBoard)


def K16_move(engineType):
    TYPES = {"K16_1": 1, "K16_2": 2, "K16_BLEND": 3}; TYPE = 2  # default type 2 (faster version)
    if engineType in TYPES:
        TYPE = TYPES[ENGINE]
    else:
        quit("That is not a valid engine type!")

    max_depth = set_depth(board) if MAX_DEPTH is None else MAX_DEPTH
    if not DEBUG: print("Calculating move...")
    start = time()
    best_move, evaluation = optimal_move(max_depth, board, engineType=TYPE, processes=PROCESSORS, end_game=is_end_game(board), debug=DEBUG)
    board.push(best_move)
    if not DEBUG:
        print(f"\nBot has played {best_move} in {round((time() - start), 3)} seconds")
    else:
        print(f"\nBot has played {best_move} with an evaluation of {round(evaluation / 100, 2)} in {round((time() - start), 3)} seconds\n")

    symbolizeAndOutput(board)

    return best_move, evaluation


def player_move():
    while True:
        input_str = input("Your move: ")

        try:
            move = board.parse_san(input_str); board.push(move)
            break
        except ValueError:
            if input_str == "pgn":
                print(chess.pgn.Game.from_board(board))
            elif input_str == "ls":
                fancyOutput = "Legal Moves - "
                for move in list(board.legal_moves):
                    fancyOutput += "\33[33m"+board.san(move)+"\x1b[0m"+" | "
                print(colored(fancyOutput.strip(), 'red'))
            else:
                print("\nIllegal move. Try again.\n")
    symbolizeAndOutput(board); print(f"{ENGINE} Engine is thinking...")


def computer_move(engineType):
    global count
    if DO_OPENING:
        count += 2
        game_line = get_mainline_moves(chess.pgn.Game.from_board(board))
        move = random_variation_move(book, game_line, count)

        if move is not None:
            board.push_san(move)
            print(f"BASE EVALUATION: {evaluate(board, engineType=1) / 100}")
            print("\n")
            symbolizeAndOutput(board)
        else:
            # print("====== END OF BOOK MOVES ======")
            K16_move(engineType)

    else:
        K16_move(engineType)


def play():
    global count
    symbolizeAndOutput(board)
    while not (board.is_game_over() or board.is_stalemate() or board.is_repetition()):
        print("Board with fen: ", board.fen())
        if board.turn == COMPUTER:
            computer_move(ENGINE)
        else:
            player_move()

if __name__ == '__main__':
    mp.freeze_support()
    side = input("Do you want to play as white (w) or black (b): ")

    COMPUTER = chess.WHITE
    if side.lower() == "w":
        COMPUTER = chess.BLACK
    elif side.lower() == "b":
        COMPUTER = chess.WHITE
    else:
        print("Invalid - must be 'w' or 'b'!")
        sleep(2)

    count = -2 if COMPUTER == chess.WHITE else -1

    try:
        play()
        # cProfile.run("play()")  # debug purposes after run
    except KeyboardInterrupt:
        print(chess.pgn.Game.from_board(board))

print(board.result())

if board.is_game_over():
    print(chess.pgn.Game.from_board(board))
