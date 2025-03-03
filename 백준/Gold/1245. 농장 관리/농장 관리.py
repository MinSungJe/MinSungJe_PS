# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)
visited = [[False for _ in range(M)] for _ in range(N)]

# DFS
def DFS(X, Y, value):
    # 탐색 불가 조건
    if X < 0 or X >= N or Y < 0 or Y >= M: return True
    if Map[X][Y] > value: return False # 봉우리가 아님
    if Map[X][Y] < value: return True
    if visited[X][Y]: return True

    # 탐색
    visited[X][Y] = True

    # 다음 탐색
    result = True
    for i in range(8):
        X_, Y_ = X+dx[i], Y+dy[i]
        result *= DFS(X_, Y_, value)

    # 봉우리 여부 반환
    return result

# 봉우리 찾기
result = 0
for x in range(N):
    for y in range(M):
        value = Map[x][y]
        if not value: continue
        if visited[x][y]: continue
        if DFS(x, y, value): result += 1

# 출력부
print(result)