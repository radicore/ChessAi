# import chess.pgn
import random
import re

# board = chess.Board()


def book_to_array():
    # Converts the txt file to a nested array containing the variation and the moves in that variation
    with open("book.txt", "r") as book:
        openings = book.read().strip().split("\n")  # for each variation
        book_moves_array = []
        for variation in openings:  # for each move in variation
            book_moves_array.append(variation.split())  # split moves and append to book_moves_array

        book.close()

    return book_moves_array


def random_variation_move(variation, mainline, i):
    matched_games = []  # Games matching the mainline game moves
    move = None
    for game in variation:
        # Check what current played moves any x variations with the same moves from book_to_array (book.txt)
        if game[:len(mainline)] == mainline[:len(mainline)]:
            matched_games.append(game)

    if len(matched_games) > 0:  # is there at least 1 variation
        return random.choice(matched_games)[i]

    return move  # No more book moves


def get_MM(pgn):  # get mainline moves (MM) from extracting specific moves from the current pgn using regex
    pgn = str(pgn).strip()
    pgn = re.sub("\[.*", "", pgn)
    pgn = re.sub("\d+\.|\*", "", pgn)
    pgn = pgn.split()
    return pgn

"""
book = book_to_array()

count = -1  # if board.turn == chess.WHITE else 0
while not board.is_game_over():
    player = board.push_san(input(": "))
    count += 2

    game_line = get_MM(chess.pgn.Game.from_board(board))
    move = random_variation_move(book, game_line, count)

    if move is not None:
        board.push_san(move)
    else:
        # print("====== END OF BOOK MOVES ======")
        board.push(random.choice(list(board.legal_moves)))
"""