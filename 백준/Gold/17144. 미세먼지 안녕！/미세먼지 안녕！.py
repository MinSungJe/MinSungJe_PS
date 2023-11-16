# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
R, C, T = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 찾기
for i in range(R):
    if Map[i][0] == -1:
        X1 = i
        X2 = i+1
        break

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 확산시키는 함수
def diffusion():
    global Map
    # 초기값 선언
    queue = deque()

    for i in range(R):
        for j in range(C):
            if Map[i][j] >= 5:
                queue.append((i,j,Map[i][j]))
    
    # 확산
    while queue:
        X, Y, value = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            X_ = X + dx[i]
            Y_ = Y + dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= R or Y_ < 0 or Y_ >= C: continue
            if Map[X_][Y_] == -1: continue

            # 확산
            Map[X_][Y_] += value // 5
            Map[X][Y] -= value // 5

# 공기청정기
def refresh(top, bottom):
    global Map
    # top
    # 왼쪽
    for i in range(top-1, 0, -1):
        Map[i][0] = Map[i-1][0]
    # 위쪽
    for j in range(0, C-1):
        Map[0][j] = Map[0][j+1]
    # 오른쪽
    for i in range(0, top):
        Map[i][C-1] = Map[i+1][C-1]
    # 아래쪽
    for j in range(C-1, 1, -1):
        Map[top][j] = Map[top][j-1]
    Map[top][1] = 0

    # bottom
    # 왼쪽
    for i in range(bottom+1, R-1):
        Map[i][0] = Map[i+1][0]
    # 아래쪽
    for j in range(0, C-1):
        Map[R-1][j] = Map[R-1][j+1]
    # 오른쪽
    for i in range(R-1, bottom, -1):
        Map[i][C-1] = Map[i-1][C-1]
    # 아래쪽
    for j in range(C-1, 1, -1):
        Map[bottom][j] = Map[bottom][j-1]
    Map[bottom][1] = 0

# 시간 보내기
for _ in range(T):
    diffusion()
    refresh(X1, X2)

# 출력부
result = 0
for row in Map:
    result += sum(row)
print(result+2)