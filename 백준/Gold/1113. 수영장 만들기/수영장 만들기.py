# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, list(input()))) for _ in range(N)]

# 전역변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# BFS로 탐색해 해당 높이의 물이 얼만큼 담기는 지 확인하는 함수
def BFS(x, y, water):
    # 초기값 선언
    count = 0
    isStored = True
    queue = deque([(x, y)])

    # BFS
    while queue:
        X, Y = queue.popleft()

        # 탐색 불가 조건
        if X < 0 or X >= N or Y < 0 or Y >= M:
            isStored = False
            continue
        if Map[X][Y] >= water: continue
        if visited[X][Y]: continue

        # 탐색
        visited[X][Y] = True
        count += 1

        # 다음 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]
            queue.append((X_, Y_))

    return count if isStored else 0

# 함수 호출
result = 0
for water in range(2, 10):
    visited = [[False for _ in range(M)] for _ in range(N)]
    for X in range(N):
        for Y in range(M):
            if Map[X][Y] >= water: continue
            if visited[X][Y]: continue
            result += BFS(X, Y, water)

# 출력부
print(result)