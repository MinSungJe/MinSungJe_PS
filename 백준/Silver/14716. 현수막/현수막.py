# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
M, N = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(M)]

# 초기값 선언
dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)
visited = [[False for _ in range(N)] for _ in range(M)]

# DFS
def DFS(X, Y):
    # 탐색 불가 조건
    if X < 0 or X >= M or Y < 0 or Y >= N: return
    if Map[X][Y] != 1: return
    if visited[X][Y]: return

    # 탐색
    visited[X][Y] = True

    # 다음 탐색
    for i in range(8):
        X_, Y_ = X+dx[i], Y+dy[i]
        DFS(X_, Y_)

# 모든 현수막 탐색
answer = 0
for x in range(M):
    for y in range(N):
        if Map[x][y] == 1 and not visited[x][y]:
            answer += 1
            DFS(x, y)

# 출력부
print(answer)