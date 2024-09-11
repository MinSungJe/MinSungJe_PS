# 입력부
N, east, west, south, north = map(int, input().split())

# 초기값 선언
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
direction = (east, west, south, north)
visited = [[False for _ in range(29)] for _ in range(29)]

# DFS
def DFS(X, Y, idx, point):
    # 단순하지 않은 경로임
    if visited[X][Y]: return 0, point * (100**(N-idx))
    # 단순한 경로임
    if idx == N: return point, point

    # 탐색
    visited[X][Y] = True

    # 다음 탐색
    dansun, total = 0, 0
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]
        dvalue, tvalue = DFS(X_, Y_, idx+1, point*direction[i])
        dansun += dvalue
        total += tvalue

    # backtracking
    visited[X][Y] = False

    return dansun, total

# 함수 호출 및 출력부
dansun, total = DFS(14, 14, 0, 1)
print(dansun/total)