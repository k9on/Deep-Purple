import Tree
import Node
'''
MCTS(Monte Calro Tree Search)

1. 선택: 현재 상태에서 특정 경로로 수읽기
2. 게임 트리의 확장: 일정 수 이상 수읽기가 진행되면 그 지점에서 한 단계 더 착수 지점을 예측
3. 시뮬레이션 : 2에서 선택한 노드에서 바둑이 종료될때까지 random으로 진행
4. 역전파: 확장된 노드의 가치를 역전파 하여 승산 가능성을 update

'''
import Tree as TR
import MakeLegalMoves as MLM
import chess
class Monte:
    def __init__(self):

        self.tree = None
        self.inputBoardString =None #처음에 입력 받은 게임의 체스보드 상태


    def set_Board(self, board):
        #몬테카를로 트리탐색 시작 전 현재 체스 보드 저장
        self.present_board= board.copy()

    def set_inputBoardString(self,str):
        #기보 형식으로 inputBoardString을 string으로 입력 받음
        self.inputBoardString = str.copy()

    def monteCarloTreeSearch(self,boardString):

        self.tree = TR.Tree(boardString) #Tree 객체 생성  #Tree의 루트 노드생성

        simulation_Number = 4 #임의의 시뮬레이션 숫자
        for i in range(simulation_Number): #수행할 시뮬레이션 횟수
            #print(self.tree.board_stack.display_Board())

            print("%s  " %(i), end='',flush=True )
            num=0
            while self.tree.get_GameOver() == False: #게임이 종료될때까지
            #tree의 currentNode가 종료 되었는지

                #다음 노드를 선택하는 확장 진행
                tempNode = self.tree.make_MonteCarloNextChild()
                self.tree.add_ChildNode(tempNode) #임의로 생성된 노드를 트리의 자식에 붙인다
                self.tree.set_CurrentNode(tempNode) # 자식이 생성 되었으므로 자식을 currentNode로 설정
                num +=1
                 #턴 넘김 swap player 자식 노드를 만들때 Push가 되어 턴이 바뀌게 되었다.
            print("몬테카를로 Depth = ",num, end='',flush=True)
            #while문을 끝나고 나왔을때 self.tree의 currentNode는 마지막 노드를 가지므로
            #currentNode부터 backpropagation을 진행하면 된다.
            self.tree.set_GameResult()
            #역전파 backbpropagation
            self.tree.backpropagation()

        #가장 좋은 수를 반환
        return self.tree.get_BestMove()

    #def get_BestMove(self):


