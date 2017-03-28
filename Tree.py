import Node
import Board_Stack.py as BS
# test
class Tree:
    def __init__(self):
        self.root_Node #
        self.penalty
        self.currentNode #현재 가리키는 노드를 임시로 저장
        self.chess_board_stack #트리에서 노드를 입력 받는보드스택

    def set_penalty(self, penalty):  # 패널티를 설정함
        self.penalty = penalty

    def go_next_node(self, node):
        # 이전 노드를 None 처리 하고 다음 순서node로 이동
        if (self.currentNode.bear_Flag == False):  # 자식을 낳은 경험이 없다면
            commands = self.currentNode.synthesize_Commands() # 명령어를 종합
            self.chess_board_strack.all_push_one(commands) # 종합된 명령어 배열을 한번에 푸쉬
            self.chess_board_strack.realize_Board()
            self.currentNode.make_Child()

        return  # Node

    def is_done(self):
        #현재 노드에서 게임 종료 확인
        return #
    def result(self, node):
        #게임종료 여부와 승패정보 반환
        return
 #   def backpropation(self, Node):
