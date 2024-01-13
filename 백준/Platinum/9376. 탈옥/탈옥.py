# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 전역변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 출발점에서 BFS 돌리는 함수
def BFS(x, y):
    # 초기값 선언
    queue = deque([(x, y, 0)])
    visited = [[-1 for _ in range(w+2)] for _ in range(h+2)]

    # BFS
    while queue:
        X, Y, count = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if X_ < 0 or X_ >= h+2 or Y_ < 0 or Y_ >= w+2: continue
            if Map[X_][Y_] == '*': continue
            if visited[X_][Y_] != -1: continue

            # 다음 탐색
            if Map[X_][Y_] == '#':
                visited[X_][Y_] = count+1
                queue.append((X_, Y_, count+1))
            else:
                visited[X_][Y_] = count
                queue.appendleft((X_, Y_, count))
    
    return visited

# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    h, w = map(int, input().split())
    # Map에 캡션넣기
    Map = [['.' for _ in range(w+2)]]
    for _ in range(h):
        Map.append(['.']+list(input())+['.'])
    Map.append(['.' for _ in range(w+2)])

    # 죄수의 위치 찾기
    pos = list()
    for i in range(1, h+1):
        for j in range(1, w+1):
            if Map[i][j] == '$': pos.append((i, j))

    # 각 위치별 여는 문의 개수 구하기 (죄수1, 죄수2, outside)
    visited_1 = BFS(pos[0][0], pos[0][1])
    visited_2 = BFS(pos[1][0], pos[1][1])
    visited_o = BFS(0, 0)

    # 결과값 계산 및 출력부
    result = 10001
    for i in range(h+2):
        for j in range(w+2):
            if visited_1[i][j] == -1 or visited_2[i][j] == -1 or visited_o[i][j] == -1: continue
            Open = visited_1[i][j] + visited_2[i][j] + visited_o[i][j]
            if Map[i][j] == '#': Open -= 2
            result = min(result, Open)
    print(result)