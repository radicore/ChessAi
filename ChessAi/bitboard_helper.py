from chess import *
from constants import *


DUAL_FILES = [  # for
    BB_FILE_A << 1,
    BB_FILE_B >> 1 | BB_FILE_B << 1,
    BB_FILE_C >> 1 | BB_FILE_C << 1,
    BB_FILE_D >> 1 | BB_FILE_D << 1,
    BB_FILE_E >> 1 | BB_FILE_E << 1,
    BB_FILE_F >> 1 | BB_FILE_F << 1,
    BB_FILE_G >> 1 | BB_FILE_G << 1,
    BB_FILE_H >> 1,
]

DUAL_SQUARES_WHITE = [  # for backed up pawns with other pawns
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    BB_A3 >> 7, BB_B3 >> 7 | BB_B3 >> 9, BB_C3 >> 7 | BB_C3 >> 9, BB_D3 >> 7 | BB_D3 >> 9, BB_E3 >> 7 | BB_E3 >> 9, BB_F3 >> 7 | BB_F3 >> 9, BB_G3 >> 7 | BB_G3 >> 9, BB_H3 >> 9,
    BB_A4 >> 7, BB_B4 >> 7 | BB_B4 >> 9, BB_C4 >> 7 | BB_C4 >> 9, BB_D4 >> 7 | BB_D4 >> 9, BB_E4 >> 7 | BB_E4 >> 9, BB_F4 >> 7 | BB_F4 >> 9, BB_G4 >> 7 | BB_G4 >> 9, BB_H4 >> 9,
    BB_A5 >> 7, BB_B5 >> 7 | BB_B5 >> 9, BB_C5 >> 7 | BB_C5 >> 9, BB_D5 >> 7 | BB_D5 >> 9, BB_E5 >> 7 | BB_E5 >> 9, BB_F5 >> 7 | BB_F5 >> 9, BB_G5 >> 7 | BB_G5 >> 9, BB_H5 >> 9,
    BB_A6 >> 7, BB_B6 >> 7 | BB_B6 >> 9, BB_C6 >> 7 | BB_C6 >> 9, BB_D6 >> 7 | BB_D6 >> 9, BB_E6 >> 7 | BB_E6 >> 9, BB_F6 >> 7 | BB_F6 >> 9, BB_G6 >> 7 | BB_G6 >> 9, BB_H6 >> 9,
    BB_A7 >> 7, BB_B7 >> 7 | BB_B7 >> 9, BB_C7 >> 7 | BB_C7 >> 9, BB_D7 >> 7 | BB_D7 >> 9, BB_E7 >> 7 | BB_E7 >> 9, BB_F7 >> 7 | BB_F7 >> 9, BB_G7 >> 7 | BB_G7 >> 9, BB_H7 >> 9,
    0, 0, 0, 0, 0, 0, 0, 0,
]

DUAL_SQUARES_BLACK = [
    0, 0, 0, 0, 0, 0, 0, 0,
    BB_A2 << 9, BB_B2 << 9 | BB_B2 << 7, BB_C2 << 9 | BB_C2 << 7, BB_D2 << 9 | BB_D2 << 7, BB_E2 << 9 | BB_E2 << 7, BB_F2 << 9 | BB_F2 << 7, BB_G2 << 9 | BB_G2 << 7, BB_H2 << 7,
    BB_A3 << 9, BB_B3 << 9 | BB_B3 << 7, BB_C3 << 9 | BB_C3 << 7, BB_D3 << 9 | BB_D3 << 7, BB_E3 << 9 | BB_E3 << 7, BB_F3 << 9 | BB_F3 << 7, BB_G3 << 9 | BB_G3 << 7, BB_H3 << 7,
    BB_A4 << 9, BB_B4 << 9 | BB_B4 << 7, BB_C4 << 9 | BB_C4 << 7, BB_D4 << 9 | BB_D4 << 7, BB_E4 << 9 | BB_E4 << 7, BB_F4 << 9 | BB_F4 << 7, BB_G4 << 9 | BB_G4 << 7, BB_H4 << 7,
    BB_A5 << 9, BB_B5 << 9 | BB_B5 << 7, BB_C5 << 9 | BB_C5 << 7, BB_D5 << 9 | BB_D5 << 7, BB_E5 << 9 | BB_E5 << 7, BB_F5 << 9 | BB_F5 << 7, BB_G5 << 9 | BB_G5 << 7, BB_H5 << 7,
    BB_A6 << 9, BB_B6 << 9 | BB_B6 << 7, BB_C6 << 9 | BB_C6 << 7, BB_D6 << 9 | BB_D6 << 7, BB_E6 << 9 | BB_E6 << 7, BB_F6 << 9 | BB_F6 << 7, BB_G6 << 9 | BB_G6 << 7, BB_H6 << 7,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
]


def count(bb):
    return bin(bb).count("1")


def openFileBonus(BOARD: Board, square):
    file = BB_FILES[square_file(square)]

    # if there are no pawns in the file, it is open
    # if there are only pawns on one side in the file (e.g. only black pawns and no white pawns) it is a semi-open file

    whitePawnsOnFile = BOARD.pawns & BOARD.occupied_co[WHITE] & file
    blackPawnsOnFile = BOARD.pawns & BOARD.occupied_co[BLACK] & file

    if (whitePawnsOnFile | blackPawnsOnFile) == 0:
        return OPEN_RAY
    if (whitePawnsOnFile == 0 and blackPawnsOnFile) != 0 or (whitePawnsOnFile != 0 and blackPawnsOnFile == 0):
        return SEMI_OPEN_RAY

    return 0


def doubledPawns(BOARD: Board):
    score = 0

    for file in BB_FILES:


        pawnsFile = BOARD.pawns & file
        whitePawns = count(BOARD.occupied_co[WHITE] & pawnsFile)
        blackPawns = count(BOARD.occupied_co[BLACK] & pawnsFile)

        if count(whitePawns) > 1:
            if file == BB_FILE_A or file == BB_FILE_H:
                score -= DOUBLED_PAWNS_PENALTY * whitePawns * 2
            else:
                score -= DOUBLED_PAWNS_PENALTY * whitePawns

        if count(blackPawns) > 1:
            if file == BB_FILE_A or file == BB_FILE_H:
                score += DOUBLED_PAWNS_PENALTY * blackPawns * 2
            else:
                score += DOUBLED_PAWNS_PENALTY * blackPawns

    return score


def openDiagonalBonus(BOARD: Board, square):
    diagonal = BB_DIAG_MASKS[square]

    # if there are no pawns in the diagonal, it is open
    # if there are only pawns on one side in the diagonal (e.g. only black pawns and no white pawns) it is a semi-open diagonal

    whitePawnsOnFile = BOARD.pawns & BOARD.occupied_co[WHITE] & diagonal
    blackPawnsOnFile = BOARD.pawns & BOARD.occupied_co[BLACK] & diagonal

    if (whitePawnsOnFile | blackPawnsOnFile) == 0:
        return OPEN_RAY
    if (whitePawnsOnFile == 0 and blackPawnsOnFile) != 0 or (whitePawnsOnFile != 0 and blackPawnsOnFile == 0):
        return SEMI_OPEN_RAY

    return 0


def isolatedPawns(BOARD: Board):
    score = 0

    # board.occupied_co[WHITE] & board.pawns & BB_FILE_E

    whitePawns = BOARD.pawns & BOARD.occupied_co[WHITE]
    blackPawns = BOARD.pawns & BOARD.occupied_co[BLACK]

    for file, BB_FILE in enumerate(BB_FILES):
        if (whitePawns & BB_FILE) != 0:
            if (DUAL_FILES[file] & whitePawns) == 0:
                score -= ISOLATED_PAWNS_PENALTY
        if (blackPawns & BB_FILE) != 0:
            if (DUAL_FILES[file] & blackPawns) == 0:
                score += ISOLATED_PAWNS_PENALTY

    return score


def pawnChains(BOARD: Board):
    score = 0

    whitePawns = BOARD.pawns & BOARD.occupied_co[WHITE]
    blackPawns = BOARD.pawns & BOARD.occupied_co[BLACK]

    for square, BB_SQUARE in enumerate(BB_SQUARES):
        if (whitePawns & BB_SQUARE) != 0:
            DUAL_WHITE = DUAL_SQUARES_WHITE[square] & whitePawns
            if DUAL_WHITE != 0:
                score += count(DUAL_WHITE) * PAWN_CHAIN_BONUS
        if (blackPawns & BB_SQUARE) != 0:
            DUAL_BLACK = DUAL_SQUARES_WHITE[square] & blackPawns
            if DUAL_BLACK != 0:
                score -= count(DUAL_BLACK) * PAWN_CHAIN_BONUS

    return score

def kingSafety(BOARD: Board):
    # checks how many pawns are in-front of the kings, the more, the safer

    if (BOARD.kings & BB_FILE_A & BOARD.occupied_co[WHITE]) != 0:
        whitePawnsKing = (BOARD.kings << 7 | BOARD.kings << 8 | BOARD.kings << 9) & BOARD.occupied_co[WHITE] & BOARD.pawns
    elif (BOARD.kings & BOARD.occupied_co[WHITE] & BB_FILE_H) != 0:
        whitePawnsKing = (BOARD.kings << 7 | BOARD.kings << 8 | BOARD.kings << 9 & BB_FILE_H) & BOARD.occupied_co[WHITE] & BOARD.pawns
    else:
        whitePawnsKing = (BOARD.kings << 7 | BOARD.kings << 8 | BOARD.kings << 9) & BOARD.occupied_co[WHITE] & BOARD.pawns

    if (BOARD.kings & BB_FILE_A & BOARD.occupied_co[BLACK]) != 0:
        blackPawnsKing = -(BOARD.kings >> 7 | BOARD.kings >> 8 | BOARD.kings >> 9) & BOARD.occupied_co[BLACK] & BOARD.pawns
    elif (BOARD.kings & BOARD.occupied_co[WHITE] & BB_FILE_H) != 0:
        blackPawnsKing = -(BOARD.kings >> 7 | BOARD.kings >> 8 | BOARD.kings >> 9 & BB_FILE_H) & BOARD.occupied_co[BLACK] & BOARD.pawns
    else:
        blackPawnsKing = -(BOARD.kings >> 7 | BOARD.kings >> 8 | BOARD.kings >> 9) & BOARD.occupied_co[BLACK] & BOARD.pawns

    total = abs(count(whitePawnsKing)-count(blackPawnsKing)) * KING_PAWN_TROPISM

    return total

