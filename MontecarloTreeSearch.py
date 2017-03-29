'''
MCTS(Monte Calro Tree Search)

1. 선택: 현재 상태에서 특정 경로로 수읽기
2. 게임 트리의 확장: 일정 수 이상 수읽기가 진행되면 그 지점에서 한 단계 더 착수 지점을 예측
3. 시뮬레이션 : 2에서 선택한 노드에서 바둑이 종료될때까지 random으로 진행
4. 역전파: 확장된 노드의 가치를 역전파 하여 승산 가능성을 update

'''
import Tree as Tr
class Monte:
    def __init__(self):
        self.tree
        self.inputBoardString #처음에 입력 받은 게임의 체스보드 상태
    #def init_Monte(self):

    def set_Board(self, board):
        #몬테카를로 트리탐색 시작 전 현재 체스 보드 저장
        self.present_board= board.copy()

    def set_inputBoardString(self,str):
        #기보 형식으로 inputBoardString을 string으로 입력 받음
        self.inputBoardString = str.copy()

    def monteCarloTreeSearch(self, node, player):

        self.tree = Tr.Tree() #Tree 객체 생성
        self.tree.set_RootNode(self.inputBoardString) #Tree의 루트 노드생성
        self.currentNode = self.tree.get_CurrentNode() #tree의 루트 노드가 current 노드로 생성


        simulation_Number = 1000 #임의의 시뮬레이션 숫자
'''
        for i in range(simulation_Number): #수행할 시뮬레이션 횟수

            while self.currentNode.:
                다음 노드를 선택하는 확장 진행

                 현재 선택한 노드가 처음 선택된 노드일 경우에

                 시뮬레이션을 시작한 노드가 어딘지 알기 위해 기록

                 턴 넘김 swap player
            역전파 backbpropagation

        가장 좋은 수를 반환
'''
    #def get_BestMove(self):


