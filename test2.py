import tensorflow as tf
import numpy
import chess

import Board2Array as BA
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
ba = BA.Board2Array()
b = chess.Board()

test = ba.board2array(b)

print(test)

