import Board2Array as BA
import math
import random

class Node:


    def __init__(self, parent = None, command=None, policy_Score = 0): # 부모로 부터 파생 될때, 부모노드의 정보와 커맨드를 부여받음
        self.command = command  # 명령어
        self.color = None # 현재 노드의 색깔 True면 흰색, False 검은색
        self.score = 0  # 최종 스코어
        self.visit = 0  # 방문횟수
        self.policy_Score = policy_Score # 정책망
        self.win = 0  # 승
        self.draw = 0  # 무
        self.lose = 0  # 패
        self.child = []  # 자식 노드
        self.parent = parent  # 부모노드
        self.bear_Flag = False
        self.Cpuct = 3

    def set_Child(self,child):
        self.child = child

    def set_Color(self,color):
        self.color = color

    def compute_Score(self): #Node의 점수를 계산한다.
        self.score = float(self.win) / (self.win + self.draw + self.lose)

    def full_Visit(self, visit):
        if self.visit == visit:
            return True
        else :
            return False

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
    def get_Flag(self):
        return self.bear_Flag

    def on_Flag(self):
        self.bear_Flag = True

    def off_Flag(self):
        self.bear_Flag = False

    def add_Win(self, win):
        self.win += win
    def add_Draw(self,draw):
        self.draw += draw
    def add_Lose(self, lose):
        self.lose += lose
    def add_Visit(self,visit):
        self.visit += visit
    def add_ChildNode(self, node):
        self.child.append(node)

    def get_AllChild(self):  # 모든 자식 노드를 반환
        if self.bear_Flag == False:
            return -1
        elif len(self.child) == 0:
            return 0
        else:
            return self.child

    def calc_selectingScore(self):
        #win/games + C_puct * policy_Score * ( root( sigma(other child visit) / ( 1 + my visit ) )
        score = self.win/(1+ self.win+self.draw+self.lose) + self.Cpuct * self.policy_Score * math.sqrt(self.sum_otherVisit() / (1 + self.visit))
        return score

    def sum_otherVisit(self):
        sumAll = self.parent.sum_childVisit()
        return sumAll - self.visit

    def sum_childVisit(self):
        lenth = len(self.child)
        sum = 0
        for i in range(lenth):
            sum += self.child[i].visit
        return sum

    def get_bestChild(self):
        lenth = len(self.child)
        index = 0
        max = 0
        candidates = []
        for i in range(lenth):
            if max < self.child[i].calc_selectingScore():
                max = self.child[i].calc_selectingScore()
                index = i
                candidates.clear()

            elif max == self.child[i].calc_selectingScore():
                candidates.append(i)
        choice = index
        if len(candidates) != 0:
            choice = random.choice(candidates)

        return self.child[choice]


    def visited(self):
        self.visit += 1

    def should_expand(self, point):
        if self.visit == point:
            return True
        else:
            return False

    def sumChildPolicyScore(self):
        sum = 0
        for child in self.child:
            sum += child.policy_Score
        return sum

    def get_policyDistribution(self):
        scores = []
        sum = self.sumChildPolicyScore()

        for child in self.child:
            score = child.policy_Score /sum
            scores.append(score)

        return scores

    def get_bestPolicyScoreChildIndex(self):
        scores = self.get_policyDistribution()
        max = -1000
        index = -1
        for i in range(len(scores)):
            if max > scores[i]:
                max = scores[i]
                index = i
        return index

    def renew_result(self, result):
        ba = BA.Board2Array()
        result = ba.trans_result(result)


        if result == 1:  # 백승
            if not self.color:
                self.add_Win(1)
                #print("백 win1")
            else:
                self.add_Lose(1)
                #print("백 win2")

        elif result == 0:  # 무승부
            self.add_Draw(1)
            #print("draw")

        elif result == -1:  # 흑승
            if not self.color:
                self.add_Lose(1)
                #print("흑 win1")
            else:
                self.add_Win(1)
                #print("흑 win2")
        else:
            print("result is not formal")

    def For_root_choice(self):
        lenth = len(self.child)
        max = -1
        index = 0
        for i in range(lenth):
            if max < self.child[i].visit:
                max = self.child[i].visit
                #print(max)
                index = i
        return index

    def is_root(self):
        if self.parent:
            return False
        else:
            return True

    def print_childInfo(self):
        lenth = len(self.child)
        #for i in range(lenth):
            #print(i,"> win:", self.child[i].win, "loss:", self.child[i].lose, "draw:", self.child[i].draw, "command:", self.child[i].command, self.child[i].visit)