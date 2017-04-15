import Node
import chess
import Board_Stack as BS
import MakeLegalMoves as MLM
import random as rand
import randPolicy as rp
class Tree:

    def __init__(self,boardString): # 체스보드의 현재 상태를 입력받아 board_stack에 전달
        self.root_Node = None
        self.penalty = 0
        self.currentNode = None#현재 가리키는 노드를 임시로 저장
        self.board_stack = BS.Board_Stack(boardString) #MCTS에서 각노드의 명령어를 사용할 Board_Stack

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

    def make_MonteCarloNextChild(self):
        # 몬테카를로에서 다음 자식을 호출하기 위해
        #tmpBoard = chess.Board(self.currentNode.get_BoardString())  # chess. Board 생성
        tmpBoard = self.board_stack.get_ChessBoard()
        #print(tmpBoard)

        # MoveMaker에 현재 board 상태에서 생성된 legal_Moves_List 생성
        movesMaker = MLM.MovesMaker()
        movesMaker.make(tmpBoard.legal_moves.__repr__())


        # 자식을 생성하기 위해 임의로 생성된 Move
        command = movesMaker.get_RandomMove()

        newChildNode = Node.Node(self.currentNode, command)
        newChildNode.set_Color(self.board_stack.get_Color())

        return newChildNode  # 생성된 Node를 반환

    # policy
    def make_policyNextChildren(self, flip = None):
        tmpBoard = self.board_stack.get_ChessBoard()

        # 정책망에게 보드상태를 넘겨주면 가능한 moves를 넘겨 받는다.
        ######################## Random Policy #####################
        model = rp.Model(tmpBoard)
        policy_points, moves = model.get()
        ############################################################
        children = []
        lenth = len(moves)
        for i in range(lenth):
            child = Node.Node(self.currentNode, moves[i], policy_points[i])
            child.set_Color(not self.board_stack.get_Color())
            children.append(child)
        self.currentNode.set_Child(children)

        self.currentNode.on_Flag()

    # rollout
    def make_policyNextRandomChildIndex(self, board):
        children = []
        tmpNode = Node.Node(parent=None, command=None)
        tmpNode.set_Child(children)
        distribution = tmpNode.get_policyDistribution()
        flag = 0
        index = 0
        rand_num = rand.random()
        for i in distribution:
            if flag <= rand_num < flag+i:
                return index
            else:
                index += 1
                flag += i

    def make_policyNextRandomChildBoard(self, board):
        tmpBoard = board.copy()
        turn = tmpBoard.turn
        model = rp.Model(tmpBoard)
        policy_points, moves = model.get()
        children = []

        tmpNode = Node.Node(parent=None, command=None)
        lenth = len(moves)
        for i in range(lenth):
            child = Node.Node(tmpNode, moves[i], policy_points[i])
            child.set_Color(turn)
            children.append(child)
        tmpNode.set_Child(children)
        distribution = tmpNode.get_policyDistribution()
        flag = 0
        index = 0
        rand_num = rand.random()
        for i in distribution:
            if flag <= rand_num < flag+i:
                break
            else:
                index += 1
                flag += i
        childcommand = tmpNode.child[index].command
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
        self.currentNode.visited()
        self.board_stack.stack_push(self.currentNode.command)

    def go_parrent(self):
        self.currentNode = self.currentNode.get_Parent()
        self.board_stack.stack_pop()

    def get_currentBoard(self):
        return self.board_stack.get_ChessBoard()

