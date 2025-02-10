# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
W, H = map(int, input().split())
Map = [list(input()) for _ in range(H)]

# 시작 지점과 도착 지점 찾기
pos = [-1, -1, -1, -1]
for i in range(H):
    for j in range(W):
        if Map[i][j] == 'C':
            if pos[0] == -1: pos[0], pos[1] = i, j
            else: pos[2], pos[3] = i, j

# 초기값 선언
queue = deque([(pos[0], pos[1], 0, 0), (pos[0], pos[1], 1, 0), (pos[0], pos[1], 2, 0), (pos[0], pos[1], 3, 0)])
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[[-1 for _ in range(4)] for _ in range(W)] for _ in range(H)]

# BFS
while queue:
    X, Y, D, count = queue.popleft()

    # 주어진 방향대로 탐색
    X_, Y_ = X+dx[D], Y+dy[D]

    # 탐색 불가 조건
    if X_ < 0 or X_ >= H or Y_ < 0 or Y_ >= W: continue
    if Map[X_][Y_] == '*': continue
    if visited[X_][Y_][D] != -1 and visited[X_][Y_][D] <= count: continue

    # 탐색
    visited[X_][Y_][D] = count
    if X_ == pos[2] and Y_ == pos[3]: continue # 도착

    # 다음 탐색
    queue.append((X_, Y_, D, count))
    if D == 0 or D == 1:
        queue.append((X_, Y_, 2, count+1))
        queue.append((X_, Y_, 3, count+1))
    else:
        queue.append((X_, Y_, 0, count+1))
        queue.append((X_, Y_, 1, count+1))

# 결과 도출
result = 10001
for d in range(4):
    value = visited[pos[2]][pos[3]][d]
    if value == -1: continue # 해당 방향으로 레이저가 오지 않음
    result = min(result, value)

# 출력부
print(result)