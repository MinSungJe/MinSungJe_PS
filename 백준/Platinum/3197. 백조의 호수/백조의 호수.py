# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]

# 초기값 선언
visited = [[False for _ in range(C)] for _ in range(R)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 백조와 물 위치 넣기
swanPos = list()
waterPos = deque()
for i in range(R):
    for j in range(C):
        if Map[i][j] == '.': waterPos.append((i, j))
        if Map[i][j] == 'L':
            waterPos.append((i, j))
            swanPos.append((i, j))
nextSwanPos = deque([(swanPos[0][0], swanPos[0][1])])

# 백조가 만날 수 있는지 확인하는 함수
def BFS(swan):
    # 초기값 선언
    nextSwan = deque()

    # 백조 위치 BFS
    while swan:
        X, Y = swan.popleft()

        # 도착
        if X == swanPos[1][0] and Y == swanPos[1][1]: return True, deque()

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= R or Y_ < 0 or Y_ >= C: continue
            if visited[X_][Y_]: continue

            # 탐색
            if Map[X_][Y_] == 'X': nextSwan.append((X, Y)) # 이동한 백조 위치 저장
            else:
                visited[X_][Y_] = True
                swan.append((X_, Y_))

    return False, nextSwan

# 빙판이 녹는 함수
def melt(water):
    # 초기값 선언
    meltIce = deque()

    # 모든 위치에 대해 탐색
    while water:
        X, Y = water.popleft()

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= R or Y_ < 0 or Y_ >= C: continue

            # 빙판이 있으면 다음 턴에 물이 될 예정임
            if Map[X_][Y_] == 'X':
                Map[X_][Y_] = '.'
                meltIce.append((X_, Y_))

    return meltIce
        

# 결과값 계산 및 출력부
result = 0
while True:
    canMove, nextSwanPos = BFS(nextSwanPos) # 백조 이동
    if canMove: break # 백조가 만남

    waterPos = melt(waterPos) # 빙판 녹이기 및 다음 탐색할 물의 위치 저장

    result += 1 # 하루가 지남
print(result)