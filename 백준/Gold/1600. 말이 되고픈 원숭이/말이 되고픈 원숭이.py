# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
K = int(input())
W, H = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(H)]

# 초기값 선언
result = -1
dx = (-1, 1, 0, 0, -2, -2, -1, -1, 1, 1, 2, 2)
dy = (0, 0, -1, 1, -1, 1, -2, 2, -2, 2, -1, 1)
queue = deque([(0, 0, 0, 0)])
visited = [[[False for _ in range(K+1)] for _ in range(W)] for _ in range(H)]

# BFS
while queue:
    X, Y, jump, count = queue.popleft()
    
    # 도착
    if X == H-1 and Y == W-1:
        result = count
        break

    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]
        # 탐색 불가 조건
        if X_ < 0 or X_ >= H or Y_ < 0 or Y_ >= W: continue
        if Map[X_][Y_]: continue
        if visited[X_][Y_][jump]: continue

        # 탐색
        visited[X_][Y_][jump] = True

        # 다음 탐색
        queue.append((X_, Y_, jump, count+1))
    
    if jump >= K: continue
    for i in range(4, 12):
        X_, Y_ = X+dx[i], Y+dy[i]
        # 탐색 불가 조건
        if X_ < 0 or X_ >= H or Y_ < 0 or Y_ >= W: continue
        if Map[X_][Y_]: continue
        if visited[X_][Y_][jump+1]: continue

        # 탐색
        visited[X_][Y_][jump+1] = True

        # 다음 탐색
        queue.append((X_, Y_, jump+1, count+1))

# 출력부
print(result)