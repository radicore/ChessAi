import re
import chess

with open("t.txt", "r") as f:
    pgn = str(f.read())
    pgn = re.sub("\/\/ .*\n", "", pgn)
    pgn = pgn.split("\n")
    pgn = [book.split() for book in pgn]

ALL_SAN = []
for book in pgn:
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    new_book = []
    for move in book:
        t = board.san(chess.Move.from_uci(move))
        board.push_san(t)
        new_book.append(t)
    ALL_SAN.append(new_book)

with open("book_moves.txt", "w") as file:
    for book in ALL_SAN:
        things = ""
        for move in book:
            things = things + move + " "
        file.write(things+"\n")

    file.close()