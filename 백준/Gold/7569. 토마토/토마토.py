# 빠른 입력, 모듈 불러오기
import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

# 입력부
N, M, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]

# 초기값 설정
queue = deque()
visited = [[[False for _ in range(N)] for _ in range(M)] for _ in range(H)]
dz = [-1,1,0,0,0,0]
dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]
result = 0
# 익은 토마토를 찾아 시작
for i in range(H):
    for j in range(M):
        for k in range(N):
            if box[i][j][k] == 1 and not visited[i][j][k]:
                queue.append((i,j,k,0))
# BFS
while queue:
    Z, X, Y, day = queue.popleft()

    if day > result: result = day

    # 다음 탐색
    for i in range(6):
        Z_ = Z + dz[i]
        X_ = X + dx[i]
        Y_ = Y + dy[i]
        # 탐색 불가 조건
        # 1. 탐색하려는 위치가 박스 범위 밖임
        if X_ < 0 or X_ >= M or Y_ < 0 or Y_ >= N or Z_ < 0 or Z_ >= H: continue
        # 2. 탐색 위치에 익지 않은 토마토가 없음
        if box[Z_][X_][Y_] != 0: continue
        # 3. 이미 탐색한 위치임
        if visited[Z_][X_][Y_]: continue

        # 탐색
        visited[Z_][X_][Y_] = True
        box[Z_][X_][Y_] = 1

        queue.append((Z_,X_,Y_,day+1))

# 익지 않은 토마토가 있는지 체크
for i in range(H):
    for j in range(M):
        for k in range(N):
            if box[i][j][k] == 0: result = -1

# 출력부
print(result)