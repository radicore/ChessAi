import chess
from minimax import minimax_AB
from organize import order_moves
import multiprocessing as mp


def material_count(BOARD):
    return sum(1 for square in chess.SQUARES if BOARD.piece_at(square))


sr = [i for i in range(5, 17)]


def set_depth(BOARD, engineType=2):
    mc = material_count(BOARD)
    if engineType == 2:  # faster engine
        if mc == 3: return 6
        elif mc == 4: return 5
        elif mc in sr: return 4
        else: return 3
    else:
        if mc == 3: return 6
        elif mc == 4: return 5
        elif mc in sr: return 4
        else: return 3


def minimax_worker(move, BOARD, depth, alpha, beta, turn, end_game, engineType, result_queue):
    # Wrapper function for minimax_AB to work with multiprocessing
    EVAL = minimax_AB(BOARD, depth, alpha, beta, turn, end_game, engineType)
    result_queue.put((move, EVAL))


def optimal_move(max_depth, BOARD, end_game=False, engineType=2, debug=False, processes=4):
    # Iterative deepening
    best_move = None

    alpha = -float('inf')
    beta = float('inf')
    max_eval = -float('inf') if BOARD.turn else float("inf")

    with mp.Pool(processes=processes) as pool, mp.Manager() as manager:
        result_queue = manager.Queue()
        moves = order_moves(BOARD)
        for depth in range(1, max_depth + 1):
            for move in moves:
                BOARD.push(move)
                pool.apply_async(minimax_worker, args=(move, BOARD.copy(), depth, alpha, beta, BOARD.turn, end_game, engineType, result_queue))
                BOARD.pop()

            for _ in range(len(moves)):
                move, EVAL = result_queue.get()
                if BOARD.turn:
                    if EVAL > max_eval:
                        if EVAL == float("inf") and debug:
                            print("FORCED CHECKMATE FOUND IN", depth, "MOVE(S)")
                        max_eval = EVAL
                        best_move = move
                else:
                    if EVAL < max_eval:
                        if EVAL == -float("inf") and debug:
                            print("FORCED CHECKMATE FOUND IN", depth, "MOVE(S)")
                        max_eval = EVAL
                        best_move = move

            if debug: print("Depth", depth, "evaluation:", max_eval, "best move:", best_move)
            if BOARD.turn and max_eval == float("inf"): return best_move, max_eval
            elif not BOARD.turn and max_eval == -float("inf"): return best_move, max_eval

    return best_move, max_eval
