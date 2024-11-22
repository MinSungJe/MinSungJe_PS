# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
Map_ = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
result = True
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 달라진 부분 찾기
isChanged = False
for i in range(N):
    for j in range(M):
        if Map[i][j] != Map_[i][j]:
            isChanged = True
            startX, startY, value, value_ = i, j, Map[i][j], Map_[i][j]
            break
    if isChanged: break

# 값이 바뀐 경우
if isChanged:
    # 초기값 선언
    queue = deque([(startX, startY)])
    visited = [[False for _ in range(M)] for _ in range(N)]

    # 백신으로 값 바꾸기
    while queue:
        X, Y = queue.popleft()

        # 탐색 불가 조건
        if X < 0 or X >= N or Y < 0 or Y >= M: continue
        if Map[X][Y] != value: continue
        if visited[X][Y]: continue

        # 탐색
        visited[X][Y] = True
        Map[X][Y] = value_

        # 다음 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]
            queue.append((X_, Y_))
    
    # 백신 투약된 상황인지 확인하기
    for x in range(N):
        for y in range(M):
            if Map[x][y] != Map_[x][y]: result = False

# 출력부
print('YES' if result else 'NO')