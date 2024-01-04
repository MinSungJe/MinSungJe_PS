# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
r, c, d = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
clean = [[False for _ in range(M)] for _ in range(N)]
queue = deque([(r, c, d)])
result = 0

while queue:
    X, Y, direction = queue.popleft()

    # 탐색
    if not clean[X][Y]: 
        clean[X][Y] = True
        result += 1

    # 주변 공간에 더러운 구역이 있는 지 탐색
    dirty = False
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]
        if Map[X_][Y_] == 1 or clean[X_][Y_]: continue
        dirty = True
        break
    
    # 다음 탐색
    if not dirty:
        X_, Y_ = X+(-dx[direction]), Y+(-dy[direction])
        if Map[X_][Y_] == 1: break # 2-2 작동 중지
        queue.append((X_, Y_, direction)) # 2-1
    
    else:
        while True:
            # 3-1 회전
            direction -= 1
            if direction == -1: direction = 3
            X_, Y_ = X+dx[direction], Y+dy[direction]

            if Map[X_][Y_] == 1 or clean[X_][Y_]:
                continue
            
            else:
                queue.append((X_, Y_, direction)) # 3-2
                break

# 출력부
print(result)