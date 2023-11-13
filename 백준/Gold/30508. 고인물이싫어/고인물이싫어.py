# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
h, w = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
queue = deque()
visited = [[0 for _ in range(M+1)] for _ in range(N+1)]
sumVisited = [[0 for _ in range(M+1)] for _ in range(N+1)]
result = 0
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 하수구 입력
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    queue.append((x, y))
    visited[x][y] = 1

# BFS
while queue:
    X, Y = queue.popleft()

    # 4방향 탐색
    for i in range(4):
        X_ = X + dx[i]
        Y_ = Y + dy[i]

        # 탐색 불가 조건
        # 1. 탐색하려고 하는 구역은 범위를 벗어남
        if X_ <= 0 or X_ > N or Y_ <= 0 or Y_ > M: continue
        # 2. 탐색하려고 하는 구역은 전 위치보다 낮음
        if Map[X_-1][Y_-1] < Map[X-1][Y-1]: continue
        # 3. 탐색하려고 하는 구역은 이미 방문한 구역임
        if visited[X_][Y_]: continue

        # 탐색
        visited[X_][Y_] = 1

        # 다음 탐색
        queue.append((X_, Y_))

# visited 배열 누적합 구하기
for i in range(1,N+1):
    for j in range(1,M+1):
        sumVisited[i][j] = sumVisited[i-1][j] + sumVisited[i][j-1] - sumVisited[i-1][j-1] + visited[i][j]

# 누적합으로부터 발걸음이 가능한 구역 구하기
for i in range(1,N+2-h):
    for j in range(1,M+2-w):
        if sumVisited[i+h-1][j+w-1] - sumVisited[i+h-1][j-1] - sumVisited[i-1][j+w-1] + sumVisited[i-1][j-1] == h*w:
            result += 1

# 출력부
print(result)