import Tree
import Node
'''
MCTS(Monte Calro Tree Search)

1. 선택: 현재 상태에서 특정 경로로 수읽기
2. 게임 트리의 확장: 일정 수 이상 수읽기가 진행되면 그 지점에서 한 단계 더 착수 지점을 예측
3. 시뮬레이션 : 2에서 선택한 노드에서 바둑이 종료될때까지 random으로 진행
4. 역전파: 확장된 노드의 가치를 역전파 하여 승산 가능성을 update

'''

class Monte:
    def __init__(self):
        self.tree

    def asking(self, board):
        solution = str() # 가장 좋은수
        root = self.tree.Play_Tree(board) # 트리한테 결과트리의 루트를 반환
        children = root.get_AllChild() # 루트로 부터 모든 legal child를 반환
        if(len(children)==0):
            print("가능한 수가 없음")
            solution = "0"
        else:
            solution = self.decide_BestMove(children)
        return solution

    def decide_BestMove(self, children):
        '''가장 좋은 수 추출'''
        return children[0].command
