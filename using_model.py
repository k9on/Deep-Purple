import tensorflow as tf
import LoadData as LD
import numpy as np
import chess
import Board2Array as BA
import MakeLegalMoves as MLM
class policy_model:
    def __init__(self):
        self.ba = BA.Board2Array()
        self.w = self.init_weights([4, 4, 13, 20])      # 4x4x13 conv 81 outputs
        self.w2 = self.init_weights([2, 2, 81, 81])     # 2x2x81 conv, 81 outputs
        self.w3 = self.init_weights([2, 2, 81, 81])    # 2x2x81 conv, 81 outputs
        self.w4 = self.init_weights([2, 2, 81, 81])    # 2x2x81 conv, 81 outputs
        self.w5 = self.init_weights([8*8*20, 1000])    # 81 필터에 8*8 이미지
        self.w_o = self.init_weights([1000, 1])         # FC 625 inputs, 4 outputs (labels)

        self.p_keep_conv = tf.placeholder("float")
        self.p_keep_hidden = tf.placeholder("float")
        self.X = tf.placeholder("float", [None, 8, 8, 13])

        self.modelname = "./mymodel/model.ckpt"
        self.sess = tf.Session()
        #init = tf.global_variables_initializer()
       # self.sess.run(init)
        self.saver = tf.train.Saver()
        self.saver.restore(self.sess, self.modelname)
        self.py_x = self.model(self.X, self.w, self.w2, self.w3, self.w4, self.w5, self.w_o, self.p_keep_conv,
                          self.p_keep_hidden)

    def model(self,X, w, w2, w3, w4, w5, w_o, p_keep_conv, p_keep_hidden):
        l1 = tf.nn.relu(tf.nn.conv2d(X, w, strides=[1, 1, 1, 1], padding='SAME'))  # 8 8 31
        l4 = tf.reshape(l1, [-1, w5.get_shape().as_list()[0]])
        l5 = tf.nn.relu(tf.matmul(l4, w5))
        pyx = tf.matmul(l5, w_o)

        return pyx

    def init_weights(self,shape):
        return tf.Variable(tf.random_normal(shape, stddev=0.01))


    def get_Score(self,board):
        b = self.ba.board2array(board)
        input1 = np.reshape(b,[-1,8,8,13])
        trX = input1
        return self.sess.run(self.py_x, feed_dict={self.X:trX, self.p_keep_conv: 1., self.p_keep_hidden: 1.})

    def make_legalMoves(self,board):
        legal_moves = board.legal_moves
        mlm = MLM.MovesMaker()
        moves = mlm.make(legal_moves.__str__())
        return moves

    def len_moves(self,moves):
        return len(moves)

    def normalize_scores(self,scores):
        sum1 = sum(scores) + len(scores)
        for i in range(len(scores)):
            if sum1 != 0:
                scores[i] += 1
                scores[i] /= sum1


    def ask_Scores(self, board):

        scores = []
        moves = self.make_legalMoves(board)
        lenth = len(moves)
        for i in range(lenth):
            childBoard = self.realize_Board(board, moves[i])
            score = self.get_Score(childBoard)
            scores.append(score)
        self.normalize_scores(scores)

        return scores, moves

    def realize_Board(self, board, move):
        b = board.copy()
        b.push_san(move)
        return b

# tmpBoard = chess.Board()
# pm = policy_model()
# while True:
#     policy_points, moves =pm.ask_Scores(tmpBoard)
#
#     print(policy_points,moves)
