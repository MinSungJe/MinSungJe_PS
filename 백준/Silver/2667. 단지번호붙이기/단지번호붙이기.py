# 빠른 입출력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(input()) for _ in range(N)]

# 초기 변수 선언
visited = [[False for _ in range(N)] for _ in range(N)]
dx = (-1,1,0,0)
dy = (0,0,-1,1)
result = []

# DFS
def DFS(X,Y):
    global count

    # 탐색 불가 조건
    # 1. 탐색하는 곳이 좌표를 넘어섬
    if X < 0 or X >= N or Y < 0 or Y >= N: return
    # 2. 탐색하는 곳이 단지가 아님
    if Map[X][Y] == '0': return
    # 3. 이미 탐색한 단지임
    if visited[X][Y]: return

    # 탐색
    visited[X][Y] = True
    count += 1

    # 다음 탐색
    for i in range(4):
        X_ = X + dx[i]
        Y_ = Y + dy[i]
        DFS(X_, Y_)

# 좌표를 돌며 단지인 부분을 찾으면 DFS 시작점으로 결정
for i in range(N):
    for j in range(N):
        if Map[i][j] == '1' and not visited[i][j]: # 조건에 맞는 시작점 발견, count 초기화 후 DFS 시작
            count = 0
            DFS(i,j)
            result.append(count) # 결과 저장

# 출력부
result.sort()
print(len(result))
for ans in result: print(ans)