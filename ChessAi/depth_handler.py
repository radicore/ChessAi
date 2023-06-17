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
    if engineType == 2:
        if mc in [3, 4]: return 6
        elif mc in [i for i in range(5, 16)]: return 5
        else: return 4
    else:
        if mc in [3, 4]: return 6
        elif mc in [i for i in range(5, 16)]: return 4
        else: return 3


def minimax_worker(move, BOARD, depth, alpha, beta, turn, end_game, engineType, result_queue):
    EVAL = minimax_AB(BOARD, depth, alpha, beta, turn, end_game, engineType)
    result_queue.put((move, EVAL))


def optimal_move(max_depth, BOARD, end_game=False, engineType=2, debug=False, processes=4):
    best_move = None

    alpha = -INF
    beta = INF
    
    best_eval = -INF if BOARD.turn else INF

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

                alpha = max(alpha, EVAL) if BOARD.turn else alpha
                beta = min(beta, EVAL) if not BOARD.turn else beta

                # I have a hint it causes a logic error as it only checks for maximizing the current side (finding max values only)

                if BOARD.turn:
                    if EVAL > best_eval:
                        best_eval = EVAL
                        best_move = move
                        if EVAL == INF:
                            pool.terminate(), pool.join()
                            if debug:
                                print(f"FORCED CHECKMATE FOUND IN {depth} MOVE(S): {move}")
                            return move, EVAL
                else:
                    if EVAL < best_eval:
                        best_eval = EVAL
                        best_move = move
                        if EVAL == -INF:
                            pool.terminate(), pool.join()
                            if debug:
                                print(f"FORCED CHECKMATE FOUND IN {depth} MOVE(S): {move}")
                            return move, EVAL

            if best_move is None:
                return random.choice(list(BOARD.legal_moves)), best_eval

            if debug: print("Depth", depth, "Evaluation:", best_eval / 100, "Best move:", best_move)
            if BOARD.turn and best_eval == INF: return best_move, best_eval
            elif not BOARD.turn and best_eval == -INF: return best_move, best_eval

    return best_move, best_eval
