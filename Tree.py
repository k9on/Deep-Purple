import Node
import MakeLegalMoves as MLM
import chess
from copy import deepcopy


class Tree:
    def __init__(self):
        self.penalty = 0
        #self.currentNode # 현재 가리키는 노드를 임시로 저장
        self.chess_board_stack = None# 트리에서 노드를 입력 받는보드스택

    def set_penalty(self, penalty):  # 패널티를 설정함
        self.penalty = penalty

    # def go_next_node(self, node):
    #     # 이전 노드를 None 처리 하고 다음 순서node로 이동
    #     if (self.currentNode.bear_Flag == False):  # 자식을 낳은 경험이 없다면
    #         commands = self.currentNode.synthesize_Commands() # 명령어를 종합
    #         self.chess_board_strack.all_push_one(commands) # 종합된 명령어 배열을 한번에 푸쉬
    #         self.chess_board_strack.realize_Board()
    #         self.currentNode.make_Child()

        #return  # Node

    def play_tree(self, board):
        '''
        board는 Chess.Board
        board에서 받는것을 리스트로 변경하자.
        root노드는 만들어서 make_tree에 주자.
        :param board:
        :return root: make_tree에서 받은 root를 반환
        '''

        root = self.make_node()

        root.board = board(str) # board는 chess.board 임.

        root.root = True #내가 루트다.

        root.list = MLM.MovesMaker.make(board.legal_moves) # 가능한 수를 리스트로 갖자.

        return self.make_nodes(root)


    def make_node(self):
        '''
        노드 한개 만들어줭
        :return node:
        '''
        node = Node.Node()
        return node

    def make_nodes(self, present):
        '''
        내가 자식이 있으면 노드를 만들고, 자식이 없으면 부모한테 내 형제를 있는지묻고,
        내 형제가 있으면 그 형제가 위 행동을 반복한다.
        반복하다 현재상태의 부모가 root면 root를 반환해라.
        :param  parent는 Node:
        :return:
        '''


        if len(present.list) != 0: #legalmoves가 있다! 그러면 리스트만큼 자식 노드 만들어서 잇자
            #list = parent.list
            while len(list) != 0:
                command = (present.list).pop(0) #리스트중 첫번째 가능한 수 빼기
                node = self.make_node() #노드 만들기
                node.parent = present    #부모랑 자식하고 잇기
                (present.child).append(node) #부모에 자식추가하기 #원본리스트
                (present.temp_child).append(node)    #다음 자식 따라갈때 쓸 사본 리스트
                node.command = command #노드에 커맨드 저장


                #부모의 보드를 받아서 지금 현재 노드에 갱신된 노트판을 string으로 추가 *메모리감소효과
                chess_board = chess.Board(present.board)
                chess_board.push_san(command)
                node.board = chess_board.board(str)
                #현재 노드판에서 가능한수 뽑아서 리스트에 저장
                node.list = MLM.MovesMaker.make(chess_board.legal_moves)
                present.bear_Flag = True #자식 만든 경험있소

            return self.make_nodes(present.child[0]) #자식중 첫번째 놈이 새로운 트리만들러 긔긔

        # 자식을 만든 경험이 있는데 자식중 하나가 트리를 완성해서 다음 자식으로 갈때 조건을 어떻게 할것인가!?
        elif present.bear_Flag == True: #첫번재 자식노드의 자손들 다 만든후, 부모로 거슬러올라와서 두번째 자식노드가 있는지 보러 갑시다.
            if len(present.temp_child) > 1:
                node = (present.temp_child).pop(1)  # 자식하나 빼서 노드만들러 갑시다.
                return self.make_nodes(node)

        else : #legalmoves가 없으면 다음 자식으로 이동
            # 자식을 만든 경험이 없고, 먼저 트리만들었던 형제가 리스트가 없었을때,

            if len((present.parent).temp_child) > 1: #부모한테 다음 자식이 있으면
                node = ((present.parent).temp_child).pop(1) #자식하나 빼서 노드만들러 갑시다.
                return self.make_nodes(node)

            else : #    다음 자식이 없으면
                if (present.parent).root == True : #그런데 자기 부모가 root면 root를 반환해라
                    return present.root

                return self.make_nodes(present.parent) #자기 부모가 root가 아니면 부모로 가라.

    def tree_search(self, node):
        '''
        
        :param node: 
        :return: 
        '''
        # 원본리스트를 사본에 복사
        node.temp_child = deepcopy(node.child)

        if node.visit < 1: #처음 방문이면
            if len(node.child) > 0:
                #자식이 있으면
                #자식중 첫쨰부터
                (node.child[0]).visit += 1
                return self.tree_search(node.child[0])

            else :
                #자식이 없으면 다음 형제가 있는지
                if len((node.parent).temp_child) > 1:
                    #있으면
                    node = (node.parent).temp_child.pop(1)
                    return self.tree_search(node)

                else:
                    #형제도 없으면 부모가 루트인지 확인해
                    if node.parent == node.root:
                        return #빠져나오자.
                    else :
                        #부모가 root아니면 부모한테 가자.
                        return self.tree_search(node.parent)
        else:
            #방문 들렸으면 첫번째 자식은 들렸다는건데



    def is_done(self):
        #현재 노드에서 게임 종료 확인
        return #
    def result(self, node):
        #게임종료 여부와 승패정보 반환
        return
 #   def backpropation(self, Node):
