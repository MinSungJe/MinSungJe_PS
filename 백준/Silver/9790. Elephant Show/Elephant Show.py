# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 전역변수 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# DFS
def DFS(x, y):
    # 탐색 불가 조건
    if x < 0 or x >= H or y < 0 or y >= W: return 0
    if Map[x][y] == '#': return 0
    if visited[x][y]: return 0

    # 탐색
    visited[x][y] = True

    # 다음 탐색
    result = 1
    for i in range(4):
        x_, y_ = x+dx[i], y+dy[i]
        result += DFS(x_, y_)

    return result

# 입력부
while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0: break # 입력 종료
    Map = [list(input()) for _ in range(H)]

    # 시작지점 찾기
    pos = [-1, -1]
    for x in range(H):
        for y in range(W):
            if Map[x][y] == 'A': pos[0], pos[1] = x, y

    # 초기값 선언
    visited = [[False for _ in range(W)] for _ in range(H)]

    # 함수 호출 및 출력부
    result = DFS(pos[0], pos[1])
    print(result)