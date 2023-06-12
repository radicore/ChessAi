import random
from minimax import minimax_AB
from organize import order_moves
import multiprocessing as mp
from evaluation import *


def material_count(BOARD):
    return sum(1 for square in chess.SQUARES if BOARD.piece_at(square))


sr = [i for i in range(5, 18)]


def set_depth(BOARD, engineType=2):
    mc = material_count(BOARD)
    if engineType == 2:  # faster engine
        if mc in [3, 4]: return 6
        elif mc in sr: return 4
        else: return 3
    else:
        if mc == 3: return 6
        elif mc == 4: return 5
        elif mc in sr: return 4
        else: return 3


def minimax_worker(move, BOARD, depth, alpha, beta, turn, end_game, engineType, result_queue):
    EVAL = minimax_AB(BOARD, depth, alpha, beta, turn, end_game, engineType)
    result_queue.put((move, EVAL))


def optimal_move(max_depth, BOARD, end_game=False, engineType=2, debug=False, processes=4):
    print(material_score(BOARD))
    # Iterative deepening
    best_move = None

    alpha = -INF
    beta = INF
    max_eval = -INF if BOARD.turn else INF

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
                        max_eval = EVAL
                        best_move = move
                        if EVAL == INF:
                            pool.terminate(), pool.join()
                            if debug:
                                print(f"FORCED CHECKMATE FOUND IN {depth} MOVE(S): {move}")
                            return move, EVAL
                else:
                    if EVAL < max_eval:
                        max_eval = EVAL
                        best_move = move
                        if EVAL == -INF:
                            pool.terminate(), pool.join()
                            if debug:
                                print(f"FORCED CHECKMATE FOUND IN {depth} MOVE(S): {move}")
                            return move, EVAL

            if best_move is None:
                return random.choice(list(BOARD.legal_moves)), max_eval

            if debug: print("Depth", depth, "evaluation:", max_eval, "best move:", best_move)
            if BOARD.turn and max_eval == INF: return best_move, max_eval
            elif not BOARD.turn and max_eval == -INF: return best_move, max_eval

    return best_move, max_eval
