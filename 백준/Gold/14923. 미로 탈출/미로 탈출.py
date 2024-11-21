# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 좌표 입력받을 때 조정하는 함수
def parsePos(X): return int(X)-1

# 입력부
N, M = map(int, input().split())
Hx, Hy = map(parsePos, input().split())
Ex, Ey = map(parsePos, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
result = -1
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
queue = deque([(Hx, Hy, 0, 0)])
visited = [[[False, False] for _ in range(M)] for _ in range(N)]
visited[Hx][Hy][0] = True

while queue:
    X, Y, wand, count = queue.popleft()

    # 탐색 완료
    if X == Ex and Y == Ey:
        result = count
        break

    # 4방향 탐색
    for i in range(4):
        X_, Y_, wand_ = X+dx[i], Y+dy[i], wand

        # 탐색 불가 조건
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= M: continue
        if visited[X_][Y_][wand_]: continue

        # 지팡이 사용 여부 확인
        if Map[X_][Y_]:
            if wand_ == 1: continue
            wand_ = 1 # 지팡이 사용

        # 탐색
        visited[X_][Y_][wand_] = True

        # 다음 탐색
        queue.append((X_, Y_, wand_, count+1))

# 출력부
print(result)