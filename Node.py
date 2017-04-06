
class Node:


    def __init__(self, parent = None, command=None): # 부모로 부터 파생 될때, 부모노드의 정보와 커맨드를 부여받음
        self.command = command  # 명령어
        self.color = None # 현재 노드의 말 색깔 True면 흰색, False 검은색
        self.score = 0  # 초기 스코어
        self.visit = 0  # 방문횟수
        self.win = 0  # 승
        self.draw = 0  # 무
        self.lose = 0  # 패
        self.child = []  # 자식 노드
        self.parent = parent  # 부모노드
        self.bear_Flag = False

    def set_Child(self,child):
        self.child = child
    def set_Color(self,color):
        self.color =color
    def compute_Score(self): #Node의 점수를 계산한다.
        self.score = float(self.win) / (self.win + self.draw + self.lose)

    def get_Score(self):
        return self.score
    def get_Command(self):
        return self.command
    def get_Parent(self):
        return self.parent
    def get_Child(self):
        return self.child
    def get_Color(self):
        return self.color
    def get_Win(self):
        return self.win
    def get_Draw(self):
        return self.draw
    def get_Lose(self):
        return self.lose

    def add_Win(self, win):
        self.win += win
    def add_Draw(self,draw):
        self.draw += draw
    def add_Lose(self, lose):
        self.lose += lose
    def add_ChildNode(self, node):
        self.child.append(node)

    def get_AllChild(self):  # 모든 자식 노드를 반환
        childList = []  # 모든 자식 노드를 받을 배열

        while len(self.child) != 0:
            childList.append(self.child.pop())

        return childList  # 자식 노드를 반환
