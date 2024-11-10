# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[False for _ in range(C)] for _ in range(R)]

# DFS
def DFS(X, Y):
    # 탐색 불가 조건
    if X < 0 or X >= R or Y < 0 or Y >= C: return [0, 0]
    if Map[X][Y] == '#': return [0, 0]
    if visited[X][Y]: return [0, 0]

    # 탐색
    visited[X][Y] = True
    result = [0, 0]
    if Map[X][Y] == 'k': result[0] += 1
    if Map[X][Y] == 'v': result[1] += 1

    # 다음 탐색
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]
        DFS_ = DFS(X_, Y_)
        result[0] += DFS_[0]
        result[1] += DFS_[1]

    return result

# 탐색
result = [0, 0]
for x in range(R):
    for y in range(C):
        # 탐색 불가 조건
        if visited[x][y]: continue
        if Map[x][y] == '#': continue
        
        # 탐색
        sheep, wolf = DFS(x, y)
        if sheep > wolf: result[0] += sheep
        else: result[1] += wolf

# 출력부
print(*result)