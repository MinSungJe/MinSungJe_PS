# 모듈 불러오기
from collections import deque

# 입력부
N, M = map(int, input().split())
Map = list(list(input()) for _ in range(N))

# 초기값 설정
result = -1
red = [0, 0]
blue = [0, 0]
hole = [0, 0]
visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# 첫 구슬 위치 찾기
for i in range(N):
    for j in range(M):
        if Map[i][j] == 'R': red[0], red[1] = i, j
        if Map[i][j] == 'B': blue[0], blue[1] = i, j
        if Map[i][j] == 'O': hole[0], hole[1] = i, j

# 구슬이 움직이는 함수
def move(X1, Y1, X2, Y2, idx):
    redStuck = False
    blueStuck = False

    # 반복문 돌기
    while True:
        if not redStuck:
            X1_ = X1 + dx[idx]
            Y1_ = Y1 + dy[idx]
        if not blueStuck:
            X2_ = X2 + dx[idx]
            Y2_ = Y2 + dy[idx]

        # 이동 불가 조건
        if Map[X1_][Y1_] == '#': redStuck = True
        if Map[X2_][Y2_] == '#': blueStuck = True

        if Map[X1_][Y1_] == 'O':
            X1, Y1 = X1_, Y1_
            redStuck = True
        if Map[X2_][Y2_] == 'O':
            X2, Y2 = X2_, Y2_
            blueStuck = True

        if blueStuck and X1_ == X2 and Y1_ == Y2: redStuck = True
        if redStuck and X1 == X2_ and Y1 == Y2_: blueStuck = True

        # 둘다 멈췄으면 반복문 종료
        if redStuck and blueStuck: break

        # 값 최신화
        if not redStuck: X1, Y1 = X1_, Y1_
        if not blueStuck: X2, Y2 = X2_, Y2_
    
    return (X1, Y1, X2, Y2)


# BFS
queue = deque([(red[0], red[1], blue[0], blue[1], 0)])
while queue:
    rX, rY, bX, bY, count = queue.popleft()

    # 탐색 불가 조건
    if visited[rX][rY][bX][bY]: continue

    # 탐색
    visited[rX][rY][bX][bY] = True

    # 탐색 종료 조건
    if count > 10: break
    if bX == hole[0] and bY == hole[1]: continue
    if rX == hole[0] and rY == hole[1]:
        result = count
        break

    # 4방향 탐색
    for i in range(4):
        rX_, rY_, bX_, bY_ = move(rX, rY, bX, bY, i)
        queue.append((rX_, rY_, bX_, bY_, count+1))

# 출력부
print(result)