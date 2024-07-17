# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[False for _ in range(C)] for _ in range(R)]

# 물 채우는 함수
def fillWater():
    temp = deque()

    # 모든 물에 대해 탐색
    while water:
        X, Y = water.popleft()

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= R or Y_ < 0 or Y_ >= C: continue
            if Map[X_][Y_] == 'X' or Map[X_][Y_] == '*' or Map[X_][Y_] == 'D': continue

            # 탐색
            Map[X_][Y_] = '*'

            # 다음 탐색때 쓸 정보 저장
            temp.append((X_, Y_))
    
    return temp


# 비버와 물 위치 확인
water = deque()
for i in range(R):
    for j in range(C):
        if Map[i][j] == 'S':
            queue = deque([(i, j, 0)])
            visited[i][j] = True
        if Map[i][j] == '*': water.append((i, j))

# BFS
result = 'KAKTUS'
prev_count = 0
while queue:
    X, Y, count = queue.popleft()

    # 비버굴 도착
    if Map[X][Y] == 'D':
        result = count
        break

    # 물 채우기
    if count > prev_count:
        water = fillWater()
        prev_count = count
        # 비버에 물참
        if Map[X][Y] == '*': continue

    # 4방향 탐색 
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]

        # 탐색 불가 조건
        if X_ < 0 or X_ >= R or Y_ < 0 or Y_ >= C: continue
        if Map[X_][Y_] == 'X' or Map[X_][Y_] == '*': continue
        if visited[X_][Y_]: continue

        # 탐색
        visited[X_][Y_] = True

        # 다음 탐색
        queue.append((X_, Y_, count+1))

# 출력부
print(result)