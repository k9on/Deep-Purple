import tensorflow as tf
import numpy
import chess
import MakeLegalMoves as MLM

import Board2Array as BA
import random
# test = [1,2,3,4]
#
# test = tf.reshape(test,[len(test),1])
#
# sess = tf.Session()
# init = tf.global_variables_initializer()
#
# sess.run(init)
# print(sess.run(test))

# temp = numpy.zeros(28*28, dtype=numpy.float32)
#
# temp = temp.reshape(-1,28,28,1)
#
# l1 = tf.nn.max_pool(temp, ksize=[1,2,2,1], strides=[1,1,1,1], padding='SAME')
#
# print(l1)


# ba = BA.Board2Array()
# b = chess.Board()
#
# test = ba.board2array(b)
#
# print(test)
#
# b = chess.Board()
#
# lm = b.legal_moves
#
# print(lm)
#
# mlm = MLM.MovesMaker()
#
# mlm.make(lm.__str__())
# move = mlm.get_RandomMove()
# print(move)
#
# uci = b.push_san(move)
#
# print(uci)
#
# b = chess.Board()
# board = b
#
# uci = b.push_san("e4")
# b.pop()
# print(uci)
# print(b)
# print(board)

#
# def test(t):
#     if t == 1 :
#         return 1
#     else:
#         return True
# print(test(2))
# while True :
#     rand = random.random()
#
#     print(rand)
#     if rand == 0 or rand == 1 :
#         break
#

# def make_policyNextRandomChildIndex(self=None, board=None):
#     # children = policy.ask(board)
#     children = []
#
#     distribution = [0.1,0.2,0.3,0.4]
#     flag = 0
#     index = 0
#     rand_num = random.random()
#     for i in distribution:
#         if flag <= rand_num < flag + i:
#             return index
#         else:
#             index += 1
#             flag += i
#
#
#
# results = [0,0,0,0]
# while True :
#     result = make_policyNextRandomChildIndex()
#     results[result] += 1
#     sum = results[0] + results[1] + results[2] + results[3]
#     print(results[0]/sum, results[1]/sum, results[2]/sum, results[3]/sum)


