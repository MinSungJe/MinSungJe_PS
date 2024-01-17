# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 전역변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# BFS 함수
def BFS(sX, sY, tX, tY):
    # 초기값 선언
    queue = deque([(sX, sY, 0)])
    visited = [[False for _ in range(w)] for _ in range(h)]
    result = 4001

    # BFS
    while queue:
        X, Y, count = queue.popleft()

        # 도착
        if X == tX and Y == tY:
            result = count
            break

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= h or Y_ < 0 or Y_ >= w: continue
            if Map[X_][Y_] == 'x': continue
            if visited[X_][Y_]: continue

            # 탐색
            visited[X_][Y_] = True

            # 다음 탐색
            queue.append((X_, Y_, count+1))
    
    return result

# DFS 완전탐색(+DP)
def DFS(X, Y, visited):
    if visited == (1<<len(dirty))-1: return 0
    if DP[X][Y][visited] != -1: return DP[X][Y][visited] # 메모이제이션
    
    result = 4001
    for target in range(len(dirty)):
        if visited & 1<<target: continue
        tX, tY = dirty[target][0], dirty[target][1]
        value = BFS(X, Y, tX, tY)

        result = min(result, value+DFS(tX, tY, visited|1<<target))

    DP[X][Y][visited] = result
    return result

while True:
    # 입력부
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    Map = [list(input()) for _ in range(h)]

    # 청소기의 위치와 더러운 곳 위치 검사
    cleaner = list()
    dirty = list()
    for i in range(h):
        for j in range(w):
            if Map[i][j] == 'o': cleaner.append((i, j))
            if Map[i][j] == '*': dirty.append((i, j))
            
    # 초기값 선언
    DP = [[[-1 for _ in range(1<<len(dirty))] for _ in range(w)] for _ in range(h)]

    # 함수 호출 및 출력부
    result = DFS(cleaner[0][0], cleaner[0][1], 0)
    print(result if result != 4001 else -1)