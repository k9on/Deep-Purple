import Node
import Board_Stack.py as BS
import MakeLegalMoves as MLM
import chess

#Montecarlo에서 MainBoard를 받아와서 작업시작00 play_Tree()
# 이제 체스판을 가져왔으니까 그게 root_Node가 되야지. set_RootNode()
# 이 상황에서 가능한 리갈무스를  찾아봐야지 Board_Stack의 get_legal_moves를 이용해서 리스트를 받고 그것을
# MakeLegalMoves로 걸러서 가능한 수만 리스트로 받자.
# 가능한 수만큼 자식 노드를 만들어줘. 필요한것, 몇명인지? 알아야지


class Tree:
    def __init__(self):
        self.root_Node #
        self.penalty
        self.currentNode #현재 가리키는 노드를 임시로 저장
        self.chess_board_stack #트리에서 노드를 입력 받는보드스택
        self.ChildList = [] #자식 리스트를 저장할 리스트
        self.ChildrenNode = [] #자식노드가 들어갈 리스트

        self.MainBoard # 몬테에서 입력받은 Mainboard

    def set_penalty(self, penalty):  # 패널티를 설정함
        self.penalty = penalty


    def play_Tree(self, MainBoard):
        '''
        보드를 받아서 저장해놓고
        그 보드에서 가능한 수를 추출
        put_next_node()를 호출해서 가능한 수가 없을때까지 재귀로 호출
        가능한 모든 경우의 수를 가지고 트리만든 후에 root를 리턴하고
        return root한다
        :param MainBoard:
        :return root:
        '''
        #보드를 받아서 저장해놓고
        temp = BS.Board_Stack()
        temp.set_mainBoard(MainBoard)
        #그 보드에서 가능한 수를 추출
        self.ChildList = MLM.MovesMaker(temp.get_legal_moves())


    def put_next_node(self, board):
        '''
        현재 보드에서 가능한 수를 체크
        가능한 수중 하나를 뽑아서
        가능한수를 리스트에 만들어서 make_child
        가능한 수가 업으면

        :param board:
        :return:
        '''
        #legalmoves가 있으면
        #legalmoves만큼 노드를 만들어서 부모 노드랑 잇고


        #legalmoves가 없으면
        return root

    def make_child(self, node):
        '''
        현재 상황에서 자식노드를 만들고,
        부모노드와 잇기
        :param node:
        :return:
        '''
        return node


    # def go_next_node(self, node):
    #     # 이전 노드를 None 처리 하고 다음 순서node로 이동
    #     if (self.currentNode.bear_Flag == False):  # 자식을 낳은 경험이 없다면
    #         commands = self.currentNode.synthesize_Commands() # 명령어를 종합
    #         self.chess_board_strack.all_push_one(commands) # 종합된 명령어 배열을 한번에 푸쉬
    #         self.chess_board_strack.realize_Board()
    #         self.currentNode.make_Child()
    #
    #     return  # Node




    def is_done(self):
        #현재 노드에서 게임 종료 확인
        return #
    def result(self, node):
        #게임종료 여부와 승패정보 반환
        return
 #   def backpropation(self, Node):
