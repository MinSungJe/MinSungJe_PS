# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]

# 전역변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# DFS
def DFS(X, Y):
    water = 0

    # 4방향 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]

        # 탐색 불가 조건
        if X_ < 0 or X_ >= R or Y_ < 0 or Y_ >= C or Map[X_][Y_] == '.':
            water += 1
            continue
        if visited[X_][Y_]: continue

        # 탐색
        visited[X_][Y_] = True

        # 다음 탐색
        DFS(X_, Y_)
    
    # 물이 3방향 이상인 경우 가라앉음
    if water >= 3: Map[X][Y] = '.'

# 50년이 지남(함수 호출)
visited = [[False for _ in range(C)] for _ in range(R)]
for x in range(R):
    for y in range(C):
        if Map[x][y] == 'X' and not visited[x][y]: DFS(x, y)

# 깎아내기
leftCount = 11
rightCount = 11
upCount = 11
downCount = 11

for x in range(R):
    count = 0
    for y in range(C):
        if Map[x][y] == '.': count += 1
        else: break
    leftCount = min(leftCount, count)

    count = 0
    for y in range(C-1, -1, -1):
        if Map[x][y] == '.': count += 1
        else: break
    rightCount = min(rightCount, count)

for y in range(C):
    count = 0
    for x in range(R):
        if Map[x][y] == '.': count += 1
        else: break
    upCount = min(upCount, count)

    count = 0
    for x in range(R-1, -1, -1):
        if Map[x][y] == '.': count += 1
        else: break
    downCount = min(downCount, count)

# 출력부
for x in range(R):
    if x < upCount or R-1-x < downCount: continue
    print(''.join(Map[x][leftCount:C-rightCount]))