# 빠른 입력 및 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

# 전역변수 선언
INF = 300000001
dx = ((1, 1, 0), (1, 1, 1, 0), (1, 1))
dy = ((0, 1, 1), (-1, 0, 1, 1), (-1, 0))

# DFS(+DP)
def DFS(x, y):
    if x == N: return INF
    if x == N-1 and y == 1: return Map[x][y]

    # 메모이제이션
    if DP[x][y] != INF: return DP[x][y]

    # 다음 탐색
    result = INF

    if y == 0: idx = 3
    if y == 1: idx = 4
    if y == 2: idx = 2
    for i in range(idx):
        x_ = x+dx[y][i]
        y_ = y+dy[y][i]
        value = Map[x][y] + DFS(x_, y_)
        result = min(result, value)

    # 메모이제이션
    DP[x][y] = result
    return result

# TC
test_case = 0
while True:
    # 입력부
    N = int(input())
    if N == 0: break # 종료
    Map = [list(map(int, input().split())) for _ in range(N)]

    # 초기값 선언
    test_case += 1
    DP = [[INF for _ in range(3)] for _ in range(N)]
    result = DFS(0, 1)

    # 출력부
    print(f'{test_case}. {result}')