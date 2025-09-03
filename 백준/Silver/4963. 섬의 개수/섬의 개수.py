# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 전역변수 선언
dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)

# DFS
def DFS(x, y):
    # 탐색 불가 조건
    if x < 0 or x >= h or y < 0 or y >= w: return
    if Map[x][y] == 0: return
    if visited[x][y]: return

    # 탐색
    visited[x][y] = True

    # 다음 탐색
    for i in range(8):
        x_, y_ = x+dx[i], y+dy[i]
        DFS(x_, y_)

# TC
while True:
    # 입력부
    w, h = map(int, input().split())

    # 입력 종료
    if w == 0 and h == 0: break

    # 초기값 선언
    Map = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]

    # 섬 탐색
    answer = 0
    for x in range(h):
        for y in range(w):
            if Map[x][y] == 1 and not visited[x][y]:
                answer += 1
                DFS(x, y)
    
    # 출력부
    print(answer)