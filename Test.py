import chess
import tensorflow as tf
import Board2Array as BA
import LoadData as LD
import numpy as np

testPgn = LD.pgn_reader('./test/test.pgn')
pgnIndex, pgnInput, pgnOutput, pgnResult = testPgn.get_data()


b = chess.Board()

t = np.eye(8)   #board 한판

a = np.zeros((13,8,8)) #13*8*8

print(t)

print(b)

ba = BA.Board2Array()

b = ba.board2array(b)

# b = pgnInput

print(pgnInput)

print(len(pgnInput))

# print(b)
#
#
# i = 0   #행
# j = 0   #열
# length = 0
#
# for row in range(8):
#     for col in range(8):
#         tmp = b[row * 8 + col]
#         t[i][j] = tmp
#         j += 1
#         length += 1
#         if col == 7:
#             j = 0
#             i += 1
#
#
# for step in range(13):
#     for row in range(8):
#         for col in range(8):
#             tmp = t[row][col]
#             if tmp == step:
#                 a[step][row][col] = 1
#             else:
#                 a[step][row][col] = 0
#
#
# ret = np.transpose(a, (2, 1, 0)).shape
#
# print(a)
# print(ret)
#
#
