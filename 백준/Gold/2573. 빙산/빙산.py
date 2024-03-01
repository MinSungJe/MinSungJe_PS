# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# BFS 탐색 함수
def ice(x, y):
    # 초기값 선언
    queue = deque([(x, y)])

    # BFS
    while queue:
        X, Y = queue.popleft()

        # 탐색 불가 조건
        if not Map[X][Y]: continue
        if visited[X][Y] != -1: continue

        # 탐색 및 다음탐색
        value = 0
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]
            if not Map[X_][Y_]: value += 1
            queue.append((X_, Y_))
        visited[X][Y] = value


# 빙산 개수 확인하기
result = 0
while True:
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == -1 and Map[i][j]:
                ice(i, j)
                count += 1
    if count > 1: break
    if not count:
        result = 0
        break
    
    result += 1

    # 빙산 녹이기
    for i in range(N):
        for j in range(M):
            if Map[i][j]: Map[i][j] = max(0, Map[i][j]-visited[i][j])

# 출력부
print(result)