# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 전역 변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    w, h = map(int, input().split())
    Map = [list(input()) for _ in range(h)]

    # 모든 요소의 위치 확인
    fire = deque()
    pos = [0, 0]
    for x in range(h):
        for y in range(w):
            if Map[x][y] == '*': fire.append((x, y))
            if Map[x][y] == '@': pos[0], pos[1] = x, y

    # 초기값 선언
    result = "IMPOSSIBLE"
    queue = deque([(pos[0], pos[1], 0)])
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[pos[0]][pos[1]] = True
    time = 0

    # BFS
    while queue:
        X, Y, count = queue.popleft()

        # 시간이 지나 불이 옮겨 붙음
        if time == count:
            time = count+1
            temp = deque()
            while fire:
                x, y = fire.popleft()

                # 4방향 탐색
                for i in range(4):
                    x_, y_ = x+dx[i], y+dy[i]

                    # 불이 번지지 못하는 조건
                    if x_ < 0 or x_ >= h or y_ < 0 or y_ >= w: continue
                    if Map[x_][y_] == '#' or Map[x_][y_] == '*': continue

                    # 불이 번짐
                    Map[x_][y_] = '*'
                    temp.append((x_, y_))
            # 불 정보 이전
            while temp: fire.append(temp.popleft())

        # 4방향 탐색
        for i in range(4):
            X_, Y_, count_ = X+dx[i], Y+dy[i], count+1

            # 탐색 불가 조건
            if X_ < 0 or X_ >= h or Y_ < 0 or Y_ >= w: # 탈출 성공
                result = count_
                break
            if Map[X_][Y_] == '*' or Map[X_][Y_] == '#': continue
            if visited[X_][Y_]: continue

            # 탐색
            visited[X_][Y_] = True

            # 다음 탐색
            queue.append((X_, Y_, count_))
        
        # 탈출 성공
        if result != "IMPOSSIBLE": break

    # 출력부
    print(result)