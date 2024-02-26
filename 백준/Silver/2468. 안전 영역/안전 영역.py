# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
result = 0
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# DFS
def DFS(X, Y, limit):
  # 탐색 불가 조건
  if X < 0 or X >= N or Y < 0 or Y >= N: return
  if Map[X][Y] <= limit: return
  if visited[X][Y]: return

  # 탐색
  visited[X][Y] = True

  # 다음 탐색
  for i in range(4):
    X_, Y_ = X+dx[i], Y+dy[i]
    DFS(X_, Y_, limit)

# 결과값 도출 및 출력부
for l in range(0, 101):
  count = 0
  visited = [[False for _ in range(N)] for _ in range(N)]
  for x in range(N):
    for y in range(N):
      if visited[x][y]: continue
      if Map[x][y] <= l: continue
      count += 1
      DFS(x, y, l)
  result = max(result, count)
print(result)