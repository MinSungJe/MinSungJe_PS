# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]

# 초기값 선언
dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}

# 판을 기울이는 함수
def Move(X1, Y1, X2, Y2, d):
    # 초기값 선언
    rStuck = False
    bStuck = False
    rX, rY, bX, bY = X1, Y1, X2, Y2

    while not rStuck or not bStuck:
        rX_, rY_, bX_, bY_ = rX+dx[d], rY+dy[d], bX+dx[d], bY+dy[d]

        # 구슬 이동 가능여부 확인
        if not rStuck:
            if Map[rX_][rY_] == '#': rStuck = True
            if Map[rX_][rY_] == 'O':
                rStuck = True
                rX, rY = rX_, rY_

        if not bStuck:
            if Map[bX_][bY_] == '#': bStuck = True
            if Map[bX_][bY_] == 'O':
                bStuck = True
                bX, bY = bX_, bY_
        
        # 구슬이 겹쳐진 경우
        if not rStuck and bStuck and rX_ == bX and rY_ == bY: rStuck = True
        if not bStuck and rStuck and bX_ == rX and bY_ == rY: bStuck = True

        # 구슬이 멈추지 않은 경우 이동
        if not rStuck: rX, rY = rX_, rY_
        if not bStuck: bX, bY = bX_, bY_

    return rX, rY, bX, bY

# 판에서 구슬과 구멍 위치 확인
rPos = [0, 0]
bPos = [0, 0]
for x in range(N):
    for y in range(M):
        if Map[x][y] == 'R': rPos = [x, y]
        if Map[x][y] == 'B': bPos = [x, y]

# BFS
result = ''
visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
queue = deque([(rPos[0], rPos[1], bPos[0], bPos[1], '')])
while queue:
    X1, Y1, X2, Y2, cmd = queue.popleft()

    # 탐색 종료 조건
    if Map[X2][Y2] == 'O': continue
    if Map[X1][Y1] == 'O':
        result = cmd
        break
    if visited[X1][Y1][X2][Y2]: continue

    # 탐색
    visited[X1][Y1][X2][Y2] = True

    # 다음 탐색
    for i in ('U', 'D', 'L', 'R'):
        X1_, Y1_, X2_, Y2_ = Move(X1, Y1, X2, Y2, i)
        queue.append((X1_, Y1_, X2_, Y2_, cmd+i))

# 출력부
count = len(result)
if not count or count > 10: print(-1)
else:
    print(count)
    print(result)