# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
team = dict()

# 팀정보 입력부
for _ in range(N):
    name = input()
    team[name] = list()
    count = int(input())
    for _ in range(count):
        member = input()
        team[name].append(member)

# 사전순 정렬
for teamName in team.keys(): team[teamName].sort()

# 퀴즈 맞추기
for _ in range(M):
    problemName = input()
    problemType = int(input())

    # 팀 이름이 주어진 경우
    if problemType == 0:
        for name in team[problemName]: print(name)
    
    # 멤버 이름이 주어진 경우
    if problemType == 1:
        for teamName in team.keys():
            if problemName in team[teamName]: print(teamName)