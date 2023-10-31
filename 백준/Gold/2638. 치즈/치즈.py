# 빠른 입력 및 재귀 한계 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# DFS 선언
def DFS(X, Y):
    global visited

    # 4방향 탐색
    for i in range(4):
        X_ = X + dx[i]
        Y_ = Y + dy[i]

        # 탐색 불가 조건
        # 1. 탐색하려는 구역이 범위를 벗어남
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
        # 2. 탐색하려는 구역은 치즈임
        if Map[X_][Y_] == 1:
            visited[X_][Y_] += 1
            continue
        # 3. 탐색하려는 구역은 이미 탐색한 적 있음
        if visited[X_][Y_]: continue

        # 탐색
        visited[X_][Y_] += 1

        # 다음 탐색
        DFS(X_, Y_)

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
visited = [[0 for _ in range(M)] for _ in range(N)]
result = 0
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 치즈 녹이기
while Map != visited:
    result += 1
    DFS(0,0)
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2: Map[i][j] = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]

# 결과값 출력
print(result)