import chess.pgn
import re
from random import choice

board = chess.Board()


def clean_pgn(pgn=open("book_moves.txt", "r").read(), clean=False):
    if not clean:
        pgn = pgn.strip()
        pgn = re.sub("\[.*", "", pgn)
        pgn = re.sub(" \d+\.", "", pgn)
        pgn = re.sub("\n", " ", pgn)
        pgn = re.sub("\d+\.|(1-0|0-1|1\/2-1\/2)", "", pgn)
        pgn = re.sub("(\w+)\n", r"\1", pgn)
        pgn = re.sub(" {2,}", "\n", pgn)  # matches 2+ spaces for newline for later processing
        pgn = pgn.split("\n")
        pgn.remove(pgn[0]), pgn.remove(pgn[-1])  # random empty spaces appear at the start and end, so I removed them
        pgn = [move.split() for move in pgn]
        pgn = [game for game in pgn]

    else:
        pgn = open("book_moves.txt", "r").read()
        pgn = pgn.strip()
        pgn = pgn.split("\n")
        pgn = [move.split() for move in pgn]
    return pgn


variation_pgn_split = clean_pgn(clean=True)


def get_mainline(pgn):
    pgn = str(pgn).strip()
    pgn = re.sub("\[.*", "", pgn)
    pgn = re.sub("\d+\.|\*", "", pgn)
    pgn = pgn.split()
    return pgn


def check_values(variation, main):
    matched_games = []
    for game in variation:
        if game[:len(main)] == main[:len(main)]:
            matched_games.append(game)

    return matched_games


"""with open("book_cleaner.txt", "w") as f:
    f.write(variation_pgn_clean)"""


count = -1
while not board.is_game_over():
    print(board)
    player = board.push_san(input(": "))
    count += 2
    # try except incase break ... blah

    game_line = get_mainline(chess.pgn.Game.from_board(board))

    print(game_line)

    moves = check_values(variation_pgn_split, game_line)

    if len(moves) != 0:
        move = choice(moves)[count]
        print(move)
        board.push_san(move)
    else:
        print("====== END OF BOOK MOVES ======")
        board.push(choice(list(board.legal_moves)))

