import chess


def order_moves(BOARD):
    ordered_legal_moves = []
    for move in BOARD.legal_moves:
        if BOARD.is_capture(move) or BOARD.is_en_passant(move) or (move.promotion == chess.QUEEN or move.promotion == chess.KNIGHT) or BOARD.is_checkmate() or BOARD.is_check():
            if BOARD.is_checkmate():
                return [move]
            if BOARD.is_check():
                ordered_legal_moves.insert(0, move)
            if move.promotion == chess.QUEEN:
                ordered_legal_moves.insert(1, move)
            if BOARD.is_capture(move) or BOARD.is_en_passant(move):
                ordered_legal_moves.insert(2, move)
            if move.promotion == chess.KNIGHT:
                ordered_legal_moves.insert(3, move)
            # ELSE other promotions are useless, so no need to add them (only need QUEEN or KNIGHT)
        else:
            ordered_legal_moves.append(move)

    return ordered_legal_moves
