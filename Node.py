

class Node:
    def __init__(self):
        self.command  # 명령어
        self.score # 초기 스코어
        self.visit # 방문횟수
        self.win # 승
        self.draw # 무
        self.lose # 패
        self.child = [] # 자식 노드
        self.child_num = 0
        self.parent  # 부모노드
   # def init_Node(self):


    def is_root(self):
        return True

    def make_Child(self, child):
        #가치망에 따른 결과로 / 대략 알파-베타 프루닝
        #자식노드를 생성할지 판단
        print("자식노드 입력")

    def get_Parent(self):
        return self.parent

    def get_Score(self):
        return self.score

    def get_Command(self):
        return self.command

