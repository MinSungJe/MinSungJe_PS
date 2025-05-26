# 빠른 입력 및 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M, K = map(int, input().split())

# 초기값 선언
visited = [[False for _ in range(M)] for _ in range(N)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
Map = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    Map[r-1][c-1] = 1

# DFS
def DFS(x, y):
    # 4방향 탐색
    result = 1
    for i in range(4):
        x_, y_ = x+dx[i], y+dy[i]
        # 탐색 불가 조건
        if x_ < 0 or x_ >= N or y_ < 0 or y_ >= M: continue
        if Map[x_][y_] == 0: continue
        if visited[x_][y_]: continue

        # 탐색
        visited[x_][y_] = True
        
        # 다음 탐색
        result += DFS(x_, y_)
    
    return result

# 함수 호출 및 출력부
result = 0
for x in range(N):
    for y in range(M):
        if Map[x][y] == 1 and not visited[x][y]:
            visited[x][y] = True
            value = DFS(x, y)
            result = max(value, result)
print(result)