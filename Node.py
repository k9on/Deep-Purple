

class Node:


    def __init__(self): # 독립적인 노드 생성할 때 ex) root Node 만들 때
        self.command = None  # 명령어
        self.score = 0  # 초기 스코어
        self.visit = 0  # 방문횟수
        self.win = 0  # 승
        self.draw = 0  # 무
        self.lose = 0  # 패
        self.child = []  # 자식 노드
        self.child_num = 0
        self.parent = None  # 부모노드
        self.bear_Flag = False  # 한번 자식노드를 낳았으면, 낳았었다는 표시
        # 예를 들어, 한번도 자식노드를 확장하지 않았을 때는 자식노드를 확장해야하지만
        # 자식노드를 확장했는데도 불구하고 자식노드가 없는 경우에는 마지막 노드임으로
        # 다음 노드로 탐색 대상을 옮겨야 함으로 두 노드의 구별이 필요하기 때문에 Flag를 쓸 필요가 있음

    def __init__(self, parent , command): # 부모로 부터 파생 될때, 부모노드의 정보와 커맨드를 부여받음
        self.command = command  # 명령어
        self.score = 0  # 초기 스코어
        self.visit = 0  # 방문횟수
        self.win = 0  # 승
        self.draw = 0  # 무
        self.lose = 0  # 패
        self.child = []  # 자식 노드
        self.child_num = 0
        self.parent = parent  # 부모노드
        self.bear_Flag = False

    def is_root(self):  # 루트노드인지 아닌지
            if self.parent == None : # 부모가 없으면 True
                return True
            else:
                return False # 있으면 False


    def make_Child(self, children): # legal moves를 배열로 받음 -> children
        #가치망에 따른 결과로 / 대략 알파-베타 프루닝
        #자식노드를 생성할지 판단


        while(len(children)!=0):
            self.child.append(children.pop())
            self.child_num = self.child_num + 1


    def get_Parent(self):
        return self.parent

    def update_Score(self, score):
        self.score = self.score + score


    def get_Score(self):
        return self.score

    def get_Command(self):
        return self.command
    def set_Win(self, win):
        self.win = win
    def set_Draw(self,draw):
        self.draw= draw
    def set_lose(self, lose):
        self.lose = lose


