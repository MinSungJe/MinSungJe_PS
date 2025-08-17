# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
M, N = map(int, input().split())
Map = [list(map(int, list(input()))) for _ in range(M)]

# 초기값 선언
visited = [[False for _ in range(N)] for _ in range(M)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# DFS
def DFS(x, y):
    # 탐색 불가 조건
    if x < 0 or x >= M or y < 0 or y >= N: return
    if Map[x][y] == 1: return
    if visited[x][y]: return

    # 탐색
    visited[x][y] = True

    # 다음 탐색
    for i in range(4):
        x_, y_ = x+dx[i], y+dy[i]
        DFS(x_, y_)

# 바깥에서 전류 흘려보내기
for y in range(N): DFS(0, y)

# 결론 도출 및 출력부
answer = False
for y in range(N):
    if visited[M-1][y]: answer = True
print('YES' if answer else 'NO')