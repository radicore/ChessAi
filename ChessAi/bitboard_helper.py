from chess import *


def count_pieces(bb):
    return bin(bb).count("1")


def count_rook_file_blockers(BOARD, square):
    return count_pieces(BOARD.occupied & BB_FILES[square_file(square)])-1


"""
def count_bishop_diagonal_blockers(BOARD, square):  # doesn't work. Why? its supposed to be & diagonal_squares not all light / dark squares
    if r % 2 == 0 and f % 2 != 0:
    print(f"{square_name(square)} is light")
    return 8-bin((BOARD.occupied & BB_LIGHT_SQUARES)).count("1")
else:
    print(f"{square_name(square)} is dark")
    return 8-bin((BOARD.occupied & BB_DARK_SQUARES)).count("1")
"""

