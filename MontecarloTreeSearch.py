

class Node:
    def __init__(self):
        self.move # 현재 노드의 명령어
        self.score # 초기 스코어
        self.visit # 방문횟수
        self.win # 승
        self.draw # 무
        self.lose # 패
        self.child = [] # 자식 노드
        self.parent  # 부모노드

    def DefineRoot(self):
        self.parent = None

    def Define(self, parent, move):
        self.parent = parent
        self.move = move


class Tree:
    def __init__(self):
        print()



class Monte:
    def __init__(self):
        print()