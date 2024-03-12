# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
M, N, K = map(int, input().split())

# 초기값 선언
result = list()
graph = [[0 for _ in range(N)] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 그래프 그리기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 1

# BFS 함수
def BFS(x, y):
    # 초기값 선언
    result = 0
    queue = deque([(x, y)])

    while queue:
        X, Y = queue.popleft()
        # 탐색 불가 조건
        if X < 0 or X >= M or Y < 0 or Y >= N: continue
        if graph[X][Y]: continue
        if visited[X][Y]: continue

        # 탐색
        visited[X][Y] = True
        result += 1

        # 다음 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]
            queue.append((X_, Y_))

    return result

# 결과값 도출 및 출력부
for x in range(M):
    for y in range(N):
        if not graph[x][y] and not visited[x][y]:
            result.append(BFS(x, y))
result.sort()
print(len(result))
print(*result)