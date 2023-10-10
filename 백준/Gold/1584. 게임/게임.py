# 빠른 입력 및 모듈 불러오기
import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

# 초기값 설정
result = -1
queue = deque()
Map = [[0 for _ in range(501)] for _ in range(501)]
visited = [[False for _ in range(501)] for _ in range(501)]
dx = (1,0,-1,0)
dy = (0,1,0,-1)

# 입력부
# 위험지역 설정
N = int(input())
for _ in range(N):
    X1, Y1, X2, Y2 = map(int, input().split())
    Xs = sorted([X1, X2])
    Ys = sorted([Y1, Y2])
    for Xi in range(Xs[0], Xs[1]+1):
        for Yi in range(Ys[0], Ys[1]+1):
            Map[Xi][Yi] = 1
# 죽음지역 설정
M = int(input())
for _ in range(M):
    X1, Y1, X2, Y2 = map(int, input().split())
    Xs = sorted([X1, X2])
    Ys = sorted([Y1, Y2])
    for Xi in range(Xs[0], Xs[1]+1):
        for Yi in range(Ys[0], Ys[1]+1):
            Map[Xi][Yi] = 2
# 처음은 고려안함
Map[0][0] = 0

# BFS 준비
queue.append((0,0,0))
# 0-1 BFS
while queue:
    X, Y, life = queue.popleft()

    # 도착
    if X == 500 and Y == 500:
        result = life
        break

    # 다음 탐색
    for i in range(4):
        X_ = X + dx[i]
        Y_ = Y + dy[i]
        
        # 탐색 불가 조건
        # 1. 탐색하려는 곳이 범위를 벗어남
        if X_ < 0 or X_ >= 501 or Y_ < 0 or Y_ >= 501: continue
        # 2. 탐색하려는 곳은 죽음 구역임
        if Map[X_][Y_] == 2: continue
        # 3. 탐색하려는 곳은 이미 방문한 적이 있음
        if visited[X_][Y_]: continue

        # 탐색 표시
        visited[X_][Y_] = True

        # 0-1 BFS
        # 탐색하려는 곳은 안전 구역임
        if Map[X_][Y_] == 0: queue.appendleft((X_,Y_,life))
        # 탐색하려는 곳은 위험 구역임
        if Map[X_][Y_] == 1: queue.append((X_,Y_,life+1))
    
# 출력부
print(result)