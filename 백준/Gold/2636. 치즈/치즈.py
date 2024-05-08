# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 전역 변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 녹일 치즈 확인하는 함수
def find_cheese():
    # 초기값 선언
    result = deque()
    queue = deque([(0, 0)])
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True

    # BFS
    while queue:
        X, Y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
            if visited[X_][Y_]: continue

            # 탐색
            visited[X_][Y_] = True
            # 공기랑 치즈가 맞닿음
            if Map[X_][Y_]:
                result.append((X_, Y_))
                continue

            # 다음 탐색
            queue.append((X_, Y_))

    return result

# 치즈 녹이기
def melt(queue):
    while queue:
        X, Y = queue.popleft()
        Map[X][Y] = 0

# 결과값 도출
result = 0
last_cheese = 0
while True:
    melt_cheese = find_cheese() # 녹일 치즈 확인
    if not melt_cheese: break # 치즈가 모두 녹음

    result += 1
    last_cheese = len(melt_cheese)
    melt(melt_cheese) # 치즈 실제로 녹이기

# 출력부
print(result)
print(last_cheese)