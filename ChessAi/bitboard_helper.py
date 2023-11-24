from chess import *


def count_pieces(bb):
    return bin(bb).count("1")


def xray_rook_blockers(BOARD, square):
    return count_pieces(BOARD.occupied & BB_FILES[square_file(square)])-1

