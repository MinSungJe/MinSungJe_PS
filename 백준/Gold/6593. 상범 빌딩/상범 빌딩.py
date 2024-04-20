# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 전역변수 선언
dz = (-1, 1, 0, 0, 0, 0)
dx = (0, 0, -1, 1, 0, 0)
dy = (0, 0, 0, 0, -1, 1)

# 입력부
while True:
    L, R, C = map(int, input().split())
    if not L and not R and not C: break # 입력 종료
    Map = list()
    for _ in range(L):
        temp = list()
        for _ in range(R):
            temp.append(list(input()))
        Map.append(temp)
        input()

    
    # 초기값 선언
    result = -1
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]

    # 시작지점 찾기
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if Map[i][j][k] == 'S':
                    queue = deque([(i, j, k, 0)])
                    visited[i][j][k] = True

    # BFS
    while queue:
        Z, X, Y, count = queue.popleft()

        # 도착
        if Map[Z][X][Y] == 'E':
            result = count
            break

        # 6방향 탐색
        for i in range(6):
            Z_, X_, Y_ = Z+dz[i], X+dx[i], Y+dy[i]

            # 탐색 불가 조건
            if Z_ < 0 or Z_ >= L or X_ < 0 or X_ >= R or Y_ < 0 or Y_ >= C: continue
            if Map[Z_][X_][Y_] == '#': continue
            if visited[Z_][X_][Y_]: continue

            # 탐색
            visited[Z_][X_][Y_] = True

            # 다음 탐색
            queue.append((Z_, X_, Y_, count+1))

    # 출력부
    print(f'Escaped in {result} minute(s).' if result != -1 else 'Trapped!')