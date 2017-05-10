import chess
import numpy as np
import tensorflow as tf
import os

from Board2Array import Board2Array as B2A
from OneHotEncoding import OneHotEncode as OHE

class GetMovesAndScores:
    def __init__(self):
        #입력으로 체스 보드를 받아온다

        self.promotion = 0.5 # legalmoves중에서 몇 퍼센트까지 만들지 결정 비율
        self.penalty = 0.01 # Score계산에서
        self.madeMoves = [] # 선택된 Moves의 list
        self.madeMovesScores =[] # madeMoves의 점수들이 들어 있는 list
        self.flag = True

    def model(self,CnnInput):
        W1 = tf.get_variable("W1", shape=[1, 1, 14, 128], initializer=tf.contrib.layers.xavier_initializer())
        B1 = tf.get_variable("B1", initializer=tf.random_normal([128], stddev=0.01))
        L1 = tf.nn.relu(tf.nn.conv2d(CnnInput, W1, strides=[1, 1, 1, 1], padding='SAME') + B1)

        W2 = tf.get_variable("W2", shape=[3, 3, 128, 128], initializer=tf.contrib.layers.xavier_initializer())
        B2 = tf.get_variable("B2", initializer=tf.random_normal([128], stddev=0.01))
        L2 = tf.nn.relu(tf.nn.conv2d(L1, W2, strides=[1, 1, 1, 1], padding='SAME') + B2)

        W3 = tf.get_variable("W3", shape=[3, 3, 128, 128], initializer=tf.contrib.layers.xavier_initializer())
        B3 = tf.get_variable("B3", initializer=tf.random_normal([128], stddev=0.01))
        L3 = tf.nn.relu(tf.nn.conv2d(L2, W3, strides=[1, 1, 1, 1], padding='VALID') + B3)

        FlatLayer = tf.reshape(L3, [-1, 6 * 6 * 128])
        Flat_W = tf.get_variable("Flat_W", shape=[6 * 6 * 128, 512], initializer=tf.contrib.layers.xavier_initializer())
        Flat_B = tf.get_variable("Flat_B", initializer=tf.random_normal([512], stddev=0.01))
        Flat_L = tf.nn.relu(tf.matmul(FlatLayer, Flat_W) + Flat_B)

        Flat_W2 = tf.get_variable("Flat_W2", initializer=tf.truncated_normal([512, 4096], stddev=0.01))
        Flat_B2 = tf.get_variable("Flat_B2", initializer=tf.random_normal([4096], stddev=0.01))

        hypothesis = tf.matmul(Flat_L, Flat_W2) + Flat_B2


        return tf.nn.softmax(hypothesis)

    def get_Model(self,startCnnInput):

        if self.flag == True:
            with tf.variable_scope("EndModel"):
                getSoftmax = self.model(startCnnInput)
                tf.get_variable_scope().reuse_variables() # 변수를 재사용하기 위한 방법
                self.flag =False
        else :
            with tf.variable_scope("EndModel",reuse=True):
                getSoftmax = self.model(startCnnInput)
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())

        saver = tf.train.Saver()
        ckpt = tf.train.get_checkpoint_state(os.path.dirname('./PNCheckpoint/'))
        if ckpt and ckpt.model_checkpoint_path:
            print(ckpt.model_checkpoint_path)
            saver.restore(sess, ckpt.model_checkpoint_path)
            print("\n체크포인트 파일 재사용 = ", ckpt.model_checkpoint_path)
            global_step = int(ckpt.model_checkpoint_path.rsplit('-', 1)[1])



        return sess.run(getSoftmax)
    def makeStartInput(self, chessBoard):

        startCnnInput = []
        startCnnInput.append(B2A().board2array2(chessBoard))
        startCnnInput = np.reshape(startCnnInput, [-1, 8, 8, 14])
        startCnnInput = tf.to_float(startCnnInput)

        return startCnnInput

    def makeMoves(self,chessBoard):
        startCnnInput= self.makeStartInput(chessBoard)
        softMax = self.get_Model(startCnnInput)
        softMax = np.array(softMax[0])


        softMaxArgMax = (-softMax).argsort() #내림차순으로 분류한 것을 리스트로 반환 받는다
        #softMAxArgMax는 크기별로 Index만 저장 되어있다.

        ohe = OHE()
        score = []
        moves = []
        i=0
        child =0
        print(chessBoard)
        while True:

            print(i, "번째 선택된 softmax 값 = ", softMax[softMaxArgMax[i]])
            tmpMove =self.indexToMove2(softMaxArgMax[i])
            tmpMove = chess.Move.from_uci(tmpMove)

            if tmpMove in chessBoard.legal_moves:
                print(child, "번째 선택된 child 값 = ", softMax[softMaxArgMax[i]], "  move = ", tmpMove)
                score.append(softMax[softMaxArgMax[i]])
                moves.append(self.indexToMove2(softMaxArgMax[i]))
                child+=1
            i+=1
            if child >5 :
                break

        return score, moves
    def indexToMove2(self, index):
        row1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        colomn1 = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8'}

        a = index // 64  # start 좌표
        b = index % 64  # end 좌표

        startAlphabet = a // 8  # a~h 를 나타내는 숫자
        startNumber = a % 8  # 1~8을 나타내는 숫자

        endAlphabet = b // 8  # a~h 를 나타내는 숫자
        endNumber = b % 8  # 1~8을 나타내는 숫자
        return row1[startAlphabet] + colomn1[startNumber] + row1[endAlphabet] + colomn1[endNumber]

