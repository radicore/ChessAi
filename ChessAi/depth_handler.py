import random
import multiprocessing as mp

from minimax import minimax_AB
from organize import order_moves
from chess import SQUARES
from evaluation import *


def material_count(BOARD):  # adds up how many pieces there are all together (to assist set_depth)
    return sum(1 for square in SQUARES if BOARD.piece_at(square))


def set_depth(BOARD, engineType=2):
    mc = material_count(BOARD)
    lm = len(list(BOARD.legal_moves))
    if BOARD.fen() in\
            ["8/8/8/8/3K4/2R5/1k6/8 w - - 0 1",
             "8/1k6/2R5/3K4/8/8/8/8 w - - 0 1",
             "8/6k1/5R2/4K3/8/8/8/8 w - - 0 1",
             "8/8/8/8/4K3/5R2/6k1/8 w - - 0 1"]:
        return 10

    if mc in [3, 4]:  # endgame
        depth = 6
    else:
        if engineType == 2:
            if mc in [i for i in range(6, 16+1)]:
                depth = 5
            else:
                depth = 4
        else:
            if mc in [i for i in range(6, 16+1)]:
                depth = 5
            else:
                depth = 4

    if lm <= 8 and depth != 5:
        depth += 1

    print(f"\nDEPTH SEARCH = {depth}\n")

    return depth


def minimax_worker(move, BOARD, depth, alpha, beta, turn, end_game, engineType, result_queue):
    EVAL = minimax_AB(BOARD, depth, alpha, beta, turn, end_game, engineType)
    result_queue.put((move, EVAL))


def optimal_move(max_depth, BOARD, end_game=False, engineType=2, debug=False, processes=4):
    best_move = None

    alpha = -INF
    beta = INF

    best_eval = -INF if BOARD.turn else INF

    step = 1

    if max_depth == 10: step = 10  # for known position (rook + king)

    moves = order_moves(BOARD)

    with mp.Pool(processes=processes) as pool, mp.Manager() as manager:
        result_queue = manager.Queue()
        for depth in range(1, max_depth+1, step):
            for move in moves:
                BOARD.push(move)
                pool.apply_async(minimax_worker, args=(move, BOARD.copy(), depth, alpha, beta, BOARD.turn, end_game, engineType, result_queue))
                BOARD.pop()

            for _ in range(len(moves)):
                move, EVAL = result_queue.get()

                alpha = max(alpha, EVAL) if BOARD.turn else alpha
                beta = min(beta, EVAL) if not BOARD.turn else beta

                true_depth = int(depth / 2)+1

                if BOARD.turn:
                    if EVAL > best_eval:
                        best_eval = EVAL
                        best_move = move
                        if EVAL == INF:
                            pool.terminate(), pool.join()
                            if debug:
                                print("Depth", depth, "Evaluation:", best_eval / 100, "Best move:", best_move)
                                print(f"FORCED CHECKMATE IN {true_depth} MOVE(S) - {move}")
                            return move, EVAL
                else:
                    if EVAL < best_eval:
                        best_eval = EVAL
                        best_move = move
                        if EVAL == -INF:
                            pool.terminate(), pool.join()
                            if debug:
                                print("Depth", depth, "Evaluation:", best_eval / 100, "Best move:", best_move)
                                print(f"FORCED CHECKMATE IN {true_depth} MOVE(S) - {move}")
                            return move, EVAL

            if best_move is None:
                return random.choice(list(BOARD.legal_moves)), best_eval

            if debug: print("Depth", depth, "Evaluation:", best_eval / 100, "Best move:", best_move)
            if BOARD.turn and best_eval == INF: return best_move, best_eval
            elif not BOARD.turn and best_eval == -INF: return best_move, best_eval

    """
    for depth in range(1, max_depth):  # Testing without multiprocessing module
            for move in moves:
                BOARD.push(move)
                EVAL = minimax_AB(BOARD, depth, alpha, beta, BOARD.turn, end_game, engineType)
                BOARD.pop()

                if EVAL > best_eval:
                    best_eval = EVAL
                    best_move = move
                print(depth, best_eval, best_move)
    """

    return best_move, best_eval
