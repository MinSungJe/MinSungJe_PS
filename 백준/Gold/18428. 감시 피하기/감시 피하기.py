# 모듈 불러오기
from itertools import combinations
from collections import deque

# 입력부
N = int(input())
Map = list(input().split() for _ in range(N))
empty = list()

# 초기값 설정
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# combinations를 위한 xy 좌표 얻기
for i in range(N):
    for j in range(N):
        if Map[i][j] == 'X': empty.append((i,j))

# 벽 세우기
def wall():
    M = [arr[:] for arr in Map]

    result = "NO"
    for walls in combinations(empty, 3):
        for X, Y in walls: M[X][Y] = 'O'
        if not detect(M):
            result = "YES"
            break
        for X, Y in walls: M[X][Y] = 'X' # backtracking
    
    return result

# 검사
def detect(M):
    # 초기값 선언
    result = False
    queue = deque()

    # 선생님(출발점) 찾기
    for i in range(N):
        for j in range(N):
            if M[i][j] == 'T':
                for d in range(4): queue.append((i, j, d))
    
    # BFS
    while queue:
        X, Y, D = queue.popleft()
        X_, Y_ = X + dx[D], Y + dy[D] # 주어진 방향으로 탐색

        # 탐색 불가 조건
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N: continue
        if M[X_][Y_] == 'O': continue

        # 탐색
        if M[X_][Y_] == 'S': # 학생을 찾음
            result = True
            break

        # 다음 탐색
        queue.append((X_, Y_, D))

    return result

# 출력부
print(wall())