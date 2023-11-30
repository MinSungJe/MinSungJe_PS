# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(input()) for _ in range(N)]

# 초기값 설정
cmd = {'L':(0, -1),
       'R': (0, 1),
       'U': (-1, 0),
       'D': (1, 0)}
visited = [[False for _ in range(M)] for _ in range(N)]
group = [[0 for _ in range(M)] for _ in range(N)]
marker = 1
result = 0

# DFS
def DFS(X, Y, mark):
    global result
    # 탐색 불가 조건
    if X < 0 or X >= N or Y < 0 or Y >= M: return
    if visited[X][Y] and group[X][Y] == mark: return

    # 탐색
    if group[X][Y]:
        result -= 1
        return
    visited[X][Y] = True
    group[X][Y] = mark

    # 다음 탐색
    X_ = X + cmd[Map[X][Y]][0]
    Y_ = Y + cmd[Map[X][Y]][1]
    DFS(X_, Y_, mark)

# 칸을 돌며 검사
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            result += 1
            DFS(i, j, marker)
            marker += 1

# 출력부
print(result)