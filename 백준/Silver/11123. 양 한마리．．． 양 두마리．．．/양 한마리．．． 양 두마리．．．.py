# 빠른 입력 및 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

# 전역 변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# DFS
def DFS(x, y):
    # 탐색 종료 조건
    if x < 0 or x >= H or y < 0 or y >= W: return
    if Map[x][y] == '.': return
    if visited[x][y]: return

    # 탐색
    visited[x][y] = True

    # 다음 탐색
    for i in range(4):
        x_, y_ = x+dx[i], y+dy[i]
        DFS(x_, y_)
    

# TC
T = int(input())
for _ in range(T):
    # 입력부
    H, W = map(int, input().split())
    Map = [list(input()) for _ in range(H)]

    # 초기값 선언
    answer = 0
    visited = [[False for _ in range(W)] for _ in range(H)]

    for x in range(H):
        for y in range(W):
            if Map[x][y] == '#' and not visited[x][y]:
                answer += 1
                DFS(x, y)
    
    # 출력부
    print(answer)