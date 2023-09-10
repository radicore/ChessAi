import random
import multiprocessing as mp
from minimax import minimax_AB
from organize import order_moves
from evaluation import *


def material_count(BOARD):  # adds up how many pieces there are all together (to assist set_depth)
    return sum(1 for square in SQUARES if BOARD.piece_at(square))


def set_depth(BOARD, engineType):
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
            if mc in [i for i in range(6, 15)]:
                depth = 5
            else:
                depth = 4
        else:
            if mc in [i for i in range(6, 15)]:
                depth = 5
            else:
                depth = 4

    if lm <= 8:
        depth += 1

    print(f"\nDEPTH SEARCH = {depth}\n")

    return depth


def optimal_move(max_depth, BOARD, end_game=False, engineType=2, debug=False, processes=4):
    # depth = max_depth

    step = 1

    best_move = None

    # Faster if you put best_eval, alpha and beta here than within the loop

    best_eval = -INF if BOARD.turn else INF
    alpha = -INF
    beta = INF

    if max_depth == 10: step = 10  # for known position (rook + king)

    moves = order_moves(BOARD)

    with mp.Pool(processes=processes) as pool:
        for depth in range(1, max_depth+1, step):

            results = []

            if best_move in moves:  # best move from previous iteration pushed as first move
                moves.remove(best_move)
                moves.insert(0, best_move)

            for move in moves:
                BOARD.push(move)
                result = pool.apply_async(minimax_AB, (BOARD.copy(), depth, alpha, beta, BOARD.turn, end_game, engineType))
                results.append((move, result))
                BOARD.pop()

            for result in results:
                move, EVAL = result[0], result[1].get()

                alpha = max(alpha, EVAL) if BOARD.turn else alpha
                beta = min(beta, EVAL) if not BOARD.turn else beta

                # print(alpha, beta)

                if BOARD.turn == WHITE:
                    true_depth = (depth // 2) + 1
                else:
                    true_depth = (depth // 2)

                if BOARD.turn:
                    if EVAL > best_eval and EVAL != -INF:

                        print("Depth", depth, "Evaluation:", best_eval / 100, "Best move:", best_move)
                        best_eval = EVAL
                        best_move = move
                        if EVAL == INF:
                            pool.terminate(), pool.join()  # waits for the process to finish before exiting
                            if debug:

                                print(f"FORCED CHECKMATE IN {true_depth} MOVE(S) - {move}")
                            return best_move, EVAL
                else:
                    if EVAL < best_eval and EVAL != INF:
                        print("Depth", depth, "Evaluation:", best_eval / 100, "Best move:", best_move)
                        best_eval = EVAL
                        best_move = move
                        if EVAL == -INF:
                            pool.terminate(), pool.join()
                            if debug:
                                print(f"FORCED CHECKMATE IN {true_depth} MOVE(S) - {move}")
                            return best_move, EVAL

            if best_move is None:  # no point in searching for best moves if there is 1 move available
                return random.choice(list(BOARD.legal_moves)), best_eval

            if debug: print("Depth", depth, "Evaluation:", best_eval / 100, "Best move:", best_move)


    # for depth in range(max_depth-1, max_depth):

    """depth = max_depth

    if BOARD.turn == WHITE:
        true_depth = (depth // 2) + 1
    else:
        true_depth = (depth // 2)

    for move in moves:
        BOARD.push(move)
        EVAL = minimax_AB(BOARD, depth, alpha, beta, BOARD.turn, end_game, engineType)
        BOARD.pop()
        if BOARD.turn:
            if EVAL > best_eval:
                print(best_eval, move)
                if EVAL == INF:
                    if debug:
                        print("Depth", depth, "Evaluation:", best_eval / 100, "Best move:", best_move)
                        print(f"FORCED CHECKMATE IN {true_depth} MOVE(S) - {move}")
                    return best_move, best_eval
                best_eval = EVAL
                best_move = move
                print("Depth", depth, "Evaluation:", best_eval / 100, "Best move:", best_move)
        else:
            if EVAL < best_eval:
                print(best_eval, move)
                if EVAL == INF:
                    if debug:
                        print("Depth", depth, "Evaluation:", best_eval / 100, "Best move:", best_move)
                        print(f"FORCED CHECKMATE IN {true_depth} MOVE(S) - {move}")
                    return best_move, best_eval
                best_eval = EVAL
                best_move = move
                print("Depth", depth, "Evaluation:", best_eval / 100, "Best move:", best_move)

    if best_move is None:  # no point in searching for best moves if there is 1 move available
        return random.choice(list(BOARD.legal_moves)), best_eval

    if debug: print("Depth", depth, "Evaluation:", best_eval / 100, "Best move:", best_move)"""

    return best_move, best_eval


