

class Node:
    def __init__(self):
        self.command=None # 명령어
        self.score =0 # 초기 스코어
        self.visit = 0# 방문횟수
        self.win = 0# 승
        self.draw = 0# 무
        self.lose = 0# 패
        self.child = [] # 자식 노드
        self.child_num = 0
        self.parent =None # 부모노드


    def init_Node(self ,parent , command): #노드를 초기화
        self.parent = parent
        self.command = command
        self.visit += 1

    def is_root(self): #부모노드가 없을 경우 RootNode
        if self.parent == None:
            return True

    def make_Child(self, child):
        #가치망에 따른 결과로 / 대략 알파-베타 프루닝
        #자식노드를 생성할지 판단

        self.child.append(child)
        print("자식노드 입력")

    def get_Parent(self):
        return self.parent

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


