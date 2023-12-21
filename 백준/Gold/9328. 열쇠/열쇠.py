# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 전역변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# BFS로 탐색하는 함수
def invasion():
    global attack

    # 초기값 선언
    attack = False
    count = 0
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque()

    # 시작하는 좌표 queue에 집어넣기
    for i in range(h):
        if i == 0 or i == h-1:
            for j in range(w): queue.append((i,j))
        else:
            for j in (0, w-1): queue.append((i,j))

    # BFS
    while queue:
        X, Y = queue.popleft()

        # 탐색 불가 조건
        if X < 0 or X >= h or Y < 0 or Y >= w: continue
        if visited[X][Y]: continue
        if Map[X][Y] == '*': continue

        # 탐색
        if ord(Map[X][Y]) >= 65 and ord(Map[X][Y]) <= 90: # 탐색한 곳이 문임
            if chr(ord(Map[X][Y])+32) in key: # 열 수 있다면
                Map[X][Y] = '.'
            else: continue # 열 수 없는 경우
        if ord(Map[X][Y]) >= 97 and ord(Map[X][Y]) <= 122: # 탐색한 곳이 열쇠임
            key.append(Map[X][Y])
            Map[X][Y] = '.'
            attack = True
        if Map[X][Y] == '$': # 탐색한 곳이 서류임
            Map[X][Y] = '.'
            count += 1
        visited[X][Y] = True

        # 다음 탐색
        for i in range(4):
            X_ = X + dx[i]
            Y_ = Y + dy[i]
            queue.append((X_, Y_))
        
    # 결과값 반환
    return count

# TC
T = int(input())
for test_case in range(1, T+1):
    h, w = map(int, input().split())
    Map = [list(input()) for _ in range(h)]
    key = list(input())

    # 초기값 선언
    attack = True
    result = 0

    # 최대한 털기
    while attack: result += invasion()

    # 출력부
    print(result)