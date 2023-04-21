import chess
from minimax import minimax_AB

DEFAULT = 2


def material_count(BOARD):
    return sum(1 for square in chess.SQUARES if BOARD.piece_at(square))


def order_moves(BOARD):
    ordered_legal_moves = []
    for move in BOARD.legal_moves:
        if BOARD.is_capture(move) or (move.promotion == chess.QUEEN or move.promotion == chess.KNIGHT) or BOARD.is_checkmate() or BOARD.is_check():
            if BOARD.is_checkmate():
                return [move]
            if BOARD.is_check():
                ordered_legal_moves.insert(0, move)
            if move.promotion == chess.QUEEN:
                ordered_legal_moves.insert(1, move)
            if move.promotion == chess.KNIGHT:
                ordered_legal_moves.insert(3, move)
            if BOARD.is_capture(move):
                ordered_legal_moves.insert(2, move)
        else:
            ordered_legal_moves.append(move)

    return ordered_legal_moves


sr = [i for i in range(5, 11)]


def set_depth(BOARD, engineType=2):
    mc = material_count(BOARD)
    if engineType == 2:  # faster engine
        if mc == 3: return 8
        elif mc == 4: return 7
        elif mc in sr: return 5
        else: return 4
    else:
        if mc == 3: return 8
        elif mc == 4: return 5
        elif mc in sr: return 4
        else: return 3


def optimal_move(max_depth, BOARD, end_game=False, engineType=2, debug=False):
    # Iterative deepening
    best_move = None
    alpha = -float('inf')
    beta = float('inf')
    max_eval = -float('inf') if BOARD.turn else float("inf")

    for depth in range(1, max_depth + 1):
        moves = order_moves(BOARD)
        for move in moves:
            BOARD.push(move)
            EVAL = minimax_AB(BOARD, depth, alpha, beta, BOARD.turn, end_game=end_game, engineType=engineType)
            BOARD.pop()
            if EVAL > max_eval:
                if EVAL == float("inf") and debug:
                    print("FORCED CHECKMATE FOUND IN", depth, "MOVE(S)")
                max_eval = EVAL
                best_move = move

        if debug: print("Depth", depth, "evaluation:", max_eval, "best move:", best_move)
        if BOARD.turn and max_eval == float("inf"): return best_move, max_eval
        elif not BOARD.turn and max_eval == -float("inf"): return best_move, max_eval
    return best_move, max_eval
