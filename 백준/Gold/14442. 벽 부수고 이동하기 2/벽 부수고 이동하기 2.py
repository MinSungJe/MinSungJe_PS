# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M, K = map(int, input().split())
Map = [list(map(int, list(input()))) for _ in range(N)]

# 초기값 선언
result = -1
queue = deque([(0, 0, 0, 1)])
visited = [[[False for _ in range(K+1)] for _ in range(M)] for _ in range(N)]

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# BFS
while queue:
    X, Y, B, count = queue.popleft()

    # 도착
    if X == N-1 and Y == M-1:
        result = count
        break

    # 4방향 탐색
    for i in range(4):
        X_, Y_, B_ = X+dx[i], Y+dy[i], B

        # 탐색 불가 조건
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
        if Map[X_][Y_] == 1: # 벽인 경우
            if B_+1 > K: continue # 더 이상 벽을 부술 수 없음
            B_ += 1
        if visited[X_][Y_][B_]: continue

        # 탐색
        visited[X_][Y_][B_] = True

        # 다음 탐색
        queue.append((X_, Y_, B_, count+1))

# 출력부
print(result)