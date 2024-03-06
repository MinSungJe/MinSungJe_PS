# 빠른 입력 및 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

# 입력부
n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
results = list()
visited = [[False for _ in range(m)] for _ in range(n)]

# DFS
def DFS(X, Y):
    result = 0
    # 4방향 탐색
    for idx in range(4):
        X_, Y_ = X+dx[idx], Y+dy[idx]
        # 탐색 불가 조건
        if X_ < 0 or X_ >= n or Y_ < 0 or Y_ >= m: continue
        if not Map[X_][Y_]: continue
        if visited[X_][Y_]: continue

        # 탐색
        visited[X_][Y_] = True

        # 다음 탐색
        result += (1+DFS(X_, Y_))

    return result
        

# 탐색
for i in range(n):
    for j in range(m):
        if Map[i][j] and not visited[i][j]:
            visited[i][j] = True
            results.append(DFS(i, j) + 1)

# 출력부
print(len(results))
print(max(results) if results else 0)