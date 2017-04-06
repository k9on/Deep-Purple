import Node
import chess
import Board_Stack as BS
import MakeLegalMoves as MLM
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
#수정해야함
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
#수정해야함 +1, 올라갈때 자식노드 업데이트함
    def backpropagation(self):

        while self.currentNode.get_Parent() != None:
            #currentNode가 backpropagation으로 거슬러 올라갈때
            #currentNode의 부모노드가 None 이라면, currentNode가 root이다!!

            #처음 들어온 currentNode는 게임이 끝난 final 노드로로 승무패 저장해야 한.
            parent = self.currentNode.get_Parent() #
            parent.add_Win(self.currentNode.get_Lose())
            parent.add_Lose(self.currentNode.get_Win())
            parent.add_Draw(self.currentNode.get_Draw())
            parent.compute_Score() # 승무패를 update한 후 Score 계산

            self.currentNode = parent

            # 부모노드로 올라갔으므로 자식 명령어들을
            # pop하여 board_stack을 update
            # stack 리스트와 chess.Board() 동시에 update
            self.board_stack.stack_pop()

            #parent.set_Child(None)  #자식 노드를 버릴 때 사용
    def get_RootNode(self):
        return self.root_Node
    def get_BestMove(self):
        childList = self.root_Node.get_Child()
        print(childList)
        bestIndex = 0
        for i in range(len(self.get_RootNode().get_Child())-1):
            if childList[i].get_Score() < childList[i+1].get_Score():
                bestIndex = i+1

        #가장 점수가 높은 Node의 Command를 return
        bestMove = childList[bestIndex].get_Command()
        for i in range(len(self.get_RootNode().get_Child()) - 1):
            print("Command= %s /ChildList[%s] Score = %s / win = %s /draw = %s / lose = %s" %(childList[i].get_Command(),i, childList[i].get_Score(),childList[i].get_Win(), childList[i].get_Draw(),childList[i].get_Lose()))
        print("MCTS return Command = ",bestMove , " Score = ", childList[bestIndex].get_Score())
        return bestMove

    def get_GameOver(self):
        return self.board_stack.get_GameOver() #게임종료를 True False로 반환
    def get_Result(self):
        return self.board_stack.get_Result()
    def set_GameResult(self):
        #게임이 끝나고 승 무 패를 저장한다
        if '1-0' == self.get_Result(): #white 승
            if  self.board_stack.get_Color() == True : #현재 노드가 white라면 '승' 추가
                self.currentNode.add_Win(1)
            else : # 현재 노드가 black이라면 '패' 추가
                self.currentNode.add_Lose(1)
        elif '0-1' == self.get_Result(): # black 승
            if self.board_stack.get_Color() == True: # 현재 노드가 black이라면 '패'추가
                self.currentNode.add_Lose(1)
            else : #현재 노드가 black이라면 '승' 추가
                self.currentNode.add_Win(1)
        else: #무승부
            self.currentNode.add_Draw(1)

        self.currentNode.compute_Score()
