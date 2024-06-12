# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]

# 초기값 선언
result = False
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# DFS
def DFS(X, Y, Type, startX, startY, move):
    result = False

    # 4방향 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]

        # 탐색 불가 조건
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
        if Map[X_][Y_] != Type: continue
        if visited[X_][Y_]: continue
        
        # 와리가리 금지
        if move == 0 and i == 1: continue
        if move == 1 and i == 0: continue
        if move == 2 and i == 3: continue
        if move == 3 and i == 2: continue

        # 처음 위치 도착
        if X_ == startX and Y_ == startY:
            result = True
            break

        # 탐색
        visited[X_][Y_] = True

        # 다음 탐색
        if DFS(X_, Y_, Type, startX, startY, i):
            result = True
            break

    return result

# 모든 칸에 대해 탐색
for x in range(N):
    for y in range(M):
        visited = [[False for _ in range(M)] for _ in range(N)]
        if DFS(x, y, Map[x][y], x, y, -1):
            result = True
            break
    if result: break

# 출력부
print('Yes' if result else 'No')