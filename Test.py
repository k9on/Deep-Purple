import chess
import Board2Array as BA
import numpy as np
b = chess.Board()

t = np.eye(8)

print(t)

print(b)

ba = BA.Board2Array()

b = ba.board2array(b)

print(type(b))

# for i in range(8):
#
#
# print(b)


