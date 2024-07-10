# 빠른 입력 및 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

# 입력부
R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[False for _ in range(C)] for _ in range(R)]

# DFS
def DFS(X, Y, isEscape):
    # 현재 위치 확인
    sheep, wolf = 0, 0
    if Map[X][Y] == 'o': sheep += 1
    if Map[X][Y] == 'v': wolf += 1

    # 다음 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]
        
        # 탐색 불가 조건
        if X_ < 0 or X_ >= R or Y_ < 0 or Y_ >= C:
            isEscape = True
            continue
        if Map[X_][Y_] == '#': continue
        if visited[X_][Y_]: continue

        # 탐색
        visited[X_][Y_] = True
        
        # 다음 탐색
        sheep_, wolf_, isEscape_ = DFS(X_, Y_, isEscape)
        sheep += sheep_
        wolf += wolf_
        if isEscape_: isEscape = True

    return sheep, wolf, isEscape

# 모든 영역 탐색
sheep, wolf = 0, 0
for x in range(R):
    for y in range(C):
        if not visited[x][y] and Map[x][y] != '#':
            visited[x][y] = True
            value_sheep, value_wolf, isEscape = DFS(x, y, False)
            if isEscape: continue # 탈출한 경우는 세지 않음

            # 결과값 반영(내쫒는 경우, 잡아먹히는 경우)
            if value_sheep > value_wolf: sheep += value_sheep
            else: wolf += value_wolf

# 출력부
print(sheep, wolf)