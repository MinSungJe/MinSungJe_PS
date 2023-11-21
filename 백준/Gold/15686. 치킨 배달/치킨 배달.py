# 빠른 입력 및 모듈 불러오기
from collections import deque
from itertools import combinations
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 집, 치킨집 좌표 넣기
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1: house.append((i, j))
        if Map[i][j] == 2: chicken.append((i, j))

# 현재 치킨집 중 M개의 치킨집 리스트를 뽑아냄 -> 라이브러리 이용
chickenGroup = combinations(chicken, M)

# 치킨 거리 구하는 함수
def ckDist(x, y, chickens):
    minDist = 0
    for chicken in chickens:
        dist = abs(x-chicken[0]) + abs(y-chicken[1])
        if not minDist: minDist = dist
        else: minDist = min(minDist, dist)
    
    return minDist

# 함수 호출
result = 0
for ck in chickenGroup:
    dist = 0
    for x, y in house:
        dist += ckDist(x, y, ck)
    if not result: result = dist
    else: result = min(result, dist)

# 출력부
print(result)