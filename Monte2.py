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
import randPolicy as rp
import GetBoardString as GBS
class Monte:
    def __init__(self, repeat_num = 100, select_depth = 30, simulation_num = 1,expend_point = 5):
        self.tree = TR.Tree()  # 트리 생성
        # self.turn = self.tree.get_CurrentNode().get_Color()  # 처음 차례 # 본 모듈은 항상 백 입장이라 가정하고 수행
        self.expand_point = expend_point  # 확장 기준값
        self.select_depth = select_depth  # 선택을 종료할 깊이
        self.repeat_num = repeat_num  # 반복 수행할 횟수
        self.simulation_num = simulation_num
        self.turn = None

    def set_state(self,board_str, turn = True):
        self.tree.reset_board(board_str)
        self.turn = turn

    def predict(self):
        for i in range(self.repeat_num):
            print(i, "번쨰 탐색")

            self.tree.go_root()
            depth = 0

            # selection
            result_selection = self.selection(depth)  # selection에서 게임이 끝이 났으면 0, 끝이 안났으면 1

            if result_selection != 0: # 선택에서 게임이 끝나지 않앗으면 확장과 시뮬레이션
                # expantion
                result = self.expantion()
                if not result :
                    # simulation
                    result = self.simulation()
            else :
                result = self.tree.get_Result()
                #print(result)

            # backpropagation
            #result = self.change_Result(result)
            self.backpropagation(result)

        # choice
        choice = self.choice()
        return choice

    def change_Result(self, result):
        if self.turn :
            return result
        else :
            if result == "1-0":
                return "0-1"
            elif result == "0-1":
                return "1-0"
            else : return result
        return result

    def selection(self, depth):
        print(depth)
        # print(self.tree.get_currentBoard().legal_moves)
        # print(self.tree.currentNode.command)
        # print(self.tree.get_currentBoard())
        # print("---------------------------")
        if depth%2 == 0:  # 내차례, 내 차례는 항상 흰색이라 가정
            flip = False
        else:  # 적차례
            flip = True
            
        if self.tree.get_GameOver():  # 보드가 게임이 끝난 상태라면 ( 흰승 : 1, 검은승 : -1, 무: 0
            return 0

        else:  # 보드가 게임이 끝나지 않았다면
            if self.select_depth > depth:  # select해야할 깊이라면
                if not self.tree.currentNode.get_Flag():  # 자식노드 체크
                    # 자식 노드 생성
                    self.tree.make_policyNextChildren(flip)
                # self.tree.currentNode.print_childInfo()
                # 다음 노드로
                self.tree.go_next()

                return self.selection(depth+1) * 1

            else:  # 깊이 기준을 초과하였다면
                if self.tree.currentNode.get_Flag(): # 자식이 있으면 자식으로
                    print("자식있음")
                    # self.tree.currentNode.print_childInfo()
                    self.tree.go_next()
                    return self.selection(depth+1) * 1

                else:  # 자식이 없다면 이제 끝
                    # self.tree.currentNode.print_childInfo()
                    return 1

    def expantion(self):

        if self.tree.currentNode.should_expand(self.expand_point):
            print("expantion")
            self.tree.make_policyNextChildren()
            self.tree.go_next()
            if self.tree.board_stack.get_GameOver() :
                return self.tree.board_stack.get_Result()
            else :
                return self.expantion()
        else:
            return False

    def simulation(self):
        #print("simulation")

        tmpBoard = self.tree.get_currentBoard().copy()

        simul_count = 0
        while not tmpBoard.is_game_over():
            simul_count += 1
            print(simul_count)
            tmpBoard = self.tree.make_policyNextRandomChildBoard(tmpBoard)
            # print(tmpBoard.turn)
            # print("--------------------------------------")
            #print(tmpBoard)
            # print(tmpBoard.is_game_over())
        print(tmpBoard)
        result = tmpBoard.result()

        return result

    def backpropagation(self, result):
        if self.tree.currentNode.is_root():
            return 0
        else:
            self.tree.currentNode.renew_result(result)
            self.tree.go_parrent()
            return self.backpropagation(result)

    def choice(self):
        root = self.tree.get_RootNode()
        index = root.For_root_choice()
        self.tree.currentNode.print_childInfo()
        return root.child[index].command

