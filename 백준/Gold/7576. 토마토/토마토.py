# 빠른 입출력 및 BFS를 위한 모듈 불러오기
import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

# 입력부
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
visited = [[False for _ in range(M)] for _ in range(N)]
queue = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0

# 익은 토마토가 있는 좌표값을 queue에 넣음
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i,j,0])

# BFS 시작
while queue:
    temp = queue.popleft()
    X = temp[0]
    Y = temp[1]
    time = temp[2]

    # 시간 기록
    if result < time: result = time

    # 주변 토마토를 queue에 넣음
    for i in range(4):
        X_ = X + dx[i]
        Y_ = Y + dy[i]
        
        # 탐색 불가 조건
        # 1. 탐색 구역이 box 구격을 벗어남
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
        # 2. 탐색 구역이 이미 탐색한 토마토임
        if visited[X_][Y_]: continue
        # 3. 탐색 구역에 익지 않은 토마토가 없음
        if box[X_][Y_] != 0: continue
        
        # 탐색 및 숙성
        visited[X_][Y_] = True
        box[X_][Y_] = 1

        queue.append([X_,Y_,time+1])


# 익지 않은 토마토가 있는지 확인
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            result = -1

# 결과 출력
print(result)