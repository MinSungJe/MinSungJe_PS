# 빠른 입력 및 모듈 불러오기
from collections import deque
from itertools import combinations
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
result = 0
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[False for _ in range(M)] for _ in range(N)]

# 둘러싸였는지 확인하는 함수, DFS
def isNotSurrounded(X, Y):
    result = False
    
    # 탐색 불가 조건
    if X < 0 or X >= N or Y < 0 or Y >= M: return False
    if Map[X][Y] == 1: return False
    if visited[X][Y]: return False

    # 빈칸이면 True return
    if Map[X][Y] == 0: return True

    # 탐색
    visited[X][Y] = True

    # 다음 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]
        if isNotSurrounded(X_, Y_): result = True

    return result

# 현재 그룹에 몇 개의 돌이 있는지 확인하는 함수
def groupCount(X, Y):
    result = 1

    # 탐색 불가 조건
    if X < 0 or X >= N or Y < 0 or Y >= M: return 0
    if Map[X][Y] != 2: return 0
    if visited[X][Y]: return 0

    # 탐색
    visited[X][Y] = True

    # 다음 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]
        result += groupCount(X_, Y_)

    return result

# 돌을 둘 수 있는 곳 확인
space = list()
for i in range(N):
    for j in range(M):
        if Map[i][j] == 0: space.append((i, j))

# 모든 상대 돌 그룹 탐색
two_group = list()
for x in range(N):
    for y in range(M):
        if Map[x][y] == 2 and not visited[x][y]: two_group.append((x, y, groupCount(x, y)))

# 돌을 놓을 수 있는 모든 조합에 대해 확인
for pos in combinations(space, 2):
    X1, Y1, X2, Y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    # 돌 놓기
    Map[X1][Y1] = 1
    Map[X2][Y2] = 1

    # 초기화
    temp = 0
    visited = [[False for _ in range(M)] for _ in range(N)]

    # 모든 돌 그룹에 대해 둘러쌓인 경우 최댓값 확인
    for X, Y, value in two_group:
        if not isNotSurrounded(X, Y): temp += value
    result = max(result, temp)

    # Backtracking
    Map[X1][Y1] = 0
    Map[X2][Y2] = 0

# 출력부
print(result)