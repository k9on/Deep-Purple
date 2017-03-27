a = [ 0 * 1 for i in range(100)]

import chess

board1 = chess.Board()

print(board1)

board2 = board1.copy()

board2.push_san("e3")

print(board1)
print(board2)