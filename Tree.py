import Node
import chess
import Board_Stack as BS
import MakeLegalMoves as MLM
import random as rand
import randPolicy as rp
import using_model as UM
import tensorflow as tf
import SYH_CNN3 as CNN
import numpy as np
import Board2Array as BA


class policy_model:
    def __init__(self):
        self.ba = BA.Board2Array()
        self.w = self.init_weights([4, 4, 13, 20])      # 4x4x13 conv 81 outputs
        self.w2 = self.init_weights([2, 2, 81, 1])     # 2x2x81 conv, 81 outputs
        self.w3 = self.init_weights([2, 2, 81, 81])    # 2x2x81 conv, 81 outputs
        self.w4 = self.init_weights([2, 2, 81, 81])    # 2x2x81 conv, 81 outputs
        self.w5 = self.init_weights([8*8*20, 100])    # 81 필터에 8*8 이미지
        self.w_o = self.init_weights([100, 1])         # FC 625 inputs, 4 outputs (labels)

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
        return self.sess.run(self.py_x, feed_dict={self.X:input1, self.p_keep_conv: 1., self.p_keep_hidden: 1.})

    def make_legalMoves(self,board):
        legal_moves = board.legal_moves.__str__()
        mlm = MLM.MovesMaker()
        moves = mlm.make(legal_moves)
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
        moves = self.make_legalMoves(board)
        lenth = len(moves)
        scores = []
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

class Tree:

    def __init__(self): # 체스보드의 현재 상태를 입력받아 board_stack에 전달
        self.root_Node = None
        self.penalty = 0
        self.currentNode = None#현재 가리키는 노드를 임시로 저장
        self.board_stack = None #MCTS에서 각노드의 명령어를 사용할 Board_Stack
        self.pm = policy_model()

    def reset_board(self,boardString):
        self.board_stack = BS.Board_Stack(boardString)
        self.set_RootNode()

    def set_RootNode(self):
        self.root_Node = Node.Node(None,None) # 루트 노드 생성
        self.currentNode = self.root_Node #루트노드가 생성될 때 currentNode로 설정
        self.currentNode.set_Color(self.board_stack.get_Color())

    def go_root(self):
        self.currentNode = self.root_Node
        self.board_stack.clear_Stack()

    def set_BoardString(self,boardString):
        self.boardString = boardString

    def get_CurrentNode(self):#현재 tree가 가리키고 있는 노드 반환
        return self.currentNode

    #Board_Stack에 추가할 command를 갱신해야 함
    def set_CurrentNode(self ,node):#들어온 node를 currentNode로
        self.currentNode = node

        #입력받은 node의 명령어로 board_stack을 갱신
        self.board_stack.stack_push(node.get_Command())

    def add_ChildNode(self,node): #tree에서 currentNode에 자식 추가
        self.currentNode.add_ChildNode(node)

    # policy
    def make_policyNextChildren(self):
        tmpBoard = self.board_stack.get_ChessBoard()
        turn = tmpBoard.turn
        # 정책망에게 보드상태를 넘겨주면 가능한 moves를 넘겨 받는다.
        ######################## Random Policy #####################
        # model = rp.Model(tmpBoard)
        # policy_points, moves = model.get()
        policy_points, moves = self.pm.ask_Scores(tmpBoard)
        # pm = UM.policy_model()
        #policy_points, moves =self.pm.ask_Scores(tmpBoard)
        ############################################################
        children = []
        lenth = len(moves)
        for i in range(lenth):
            tmpBoard2 = tmpBoard.copy()
            tmpBoard2.push_san(moves[i])
            if tmpBoard2.is_game_over() :
                if turn :
                    if tmpBoard2.result() == "1-0" :
                        policy_points[i] = 1000000
                        print("백이 이기는 수")
                    elif tmpBoard2.result() == "0-1":
                        print("내가 백인데 흑이 이기는 수")
                        continue
                    elif tmpBoard2.result() == "1/2-1/2":
                        if self.check_board(tmpBoard2):
                            continue
                        print("백 : 비김")
                        print(tmpBoard2)
                else :
                    if tmpBoard2.result() == "1-0" :
                        print("내가 흑인데 백이 이기는 수")
                        continue
                    elif tmpBoard2.result() == "0-1":
                        print("흑이 이기는 수")
                        policy_points[i] = 1000000
                    elif tmpBoard2.result() == "1/2-1/2":
                        if self.check_board(tmpBoard2):
                            continue
                        print("흑 : 비김")
                        print(tmpBoard2)
            child = Node.Node(self.currentNode, moves[i], policy_points[i])
            child.set_Color(not turn)
            children.append(child)
        self.currentNode.set_Child(children)

        self.currentNode.on_Flag()

    # rollout
    def make_policyNextRandomChildBoard(self, board):
        tmpBoard = board.copy()
        turn = tmpBoard.turn
        policy_points, moves =self.pm.ask_Scores(tmpBoard)
        # model = rp.Model(tmpBoard)
        # policy_points, moves = model.get()
        children = []

        tmpNode = Node.Node(parent=None, command=None)
        lenth = len(moves)
        for i in range(lenth):
            tmpBoard2 = tmpBoard.copy()
            tmpBoard2.push_san(moves[i])
            if tmpBoard2.is_game_over():

                if turn:
                    if tmpBoard2.result() == "1-0":
                        policy_points[i] = 1000000
                        print("백이 이기는 수")
                    elif tmpBoard2.result() == "0-1":
                        print("내가 백인데 흑이 이기는 수")
                        continue
                    elif tmpBoard2.result() == "1/2-1/2":
                        if self.check_board(tmpBoard2):
                            continue
                        print("백 : 비김")
                        print(tmpBoard2)
                else:
                    if tmpBoard2.result() == "1-0":
                        print("내가 흑인데 백이 이기는 수")
                        continue
                    elif tmpBoard2.result() == "0-1":
                        print("흑이 이기는 수")
                        policy_points[i] = 1000000
                    elif tmpBoard2.result() == "1/2-1/2":
                        if self.check_board(tmpBoard2):
                            continue
                        print("흑 : 비김")
                        print(tmpBoard2)

            child = Node.Node(tmpNode, moves[i], policy_points[i])
            child.set_Color(not turn)
            children.append(child)

        tmpNode.set_Child(children)
        distribution = tmpNode.get_policyDistribution()
        #tmpNode.print_childInfo()
        #print(distribution)
        flag = 0
        index = 0
        rand_num = rand.random()
        for i in distribution:
            if flag <= rand_num < flag+i:
                break
            else:
                index += 1
                flag += i
        try :
            childcommand = tmpNode.child[index].command
        except IndexError:
            childcommand = rand.choice(moves)
        #print(childcommand)

        tmpBoard.push_san(childcommand)
        return tmpBoard

    def get_RootNode(self):
        return self.root_Node

    def get_GameOver(self):
        return self.board_stack.get_GameOver() #게임종료를 True False로 반환

    def get_Result(self):
        return self.board_stack.get_Result()

    def go_next(self):
        self.currentNode = self.currentNode.get_bestChild()
        self.currentNode.add_Visit(1)
        self.board_stack.stack_push(self.currentNode.command)

    def go_parrent(self):
        self.currentNode = self.currentNode.get_Parent()
        self.board_stack.stack_pop()

    def get_currentBoard(self):
        return self.board_stack.get_ChessBoard()

    def check_board(self,board):
        flag = False
        if board.can_claim_threefold_repetition():
            flag = True
        if board.can_claim_fifty_moves():
            flag = True
        if board.can_claim_draw():
            flag = True

        if board.is_fivefold_repetition():
            flag = True

        if board.is_seventyfive_moves():
            flag = True
        return flag