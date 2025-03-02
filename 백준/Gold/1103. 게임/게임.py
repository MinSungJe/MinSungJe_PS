# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# H가 아닌 경우 int를 넣는 함수
def setTypeNotHole(value):
    if value == 'H': return value
    return int(value)

# 입력부
N, M = map(int, input().split())
Map = [list(map(setTypeNotHole, list(input()))) for _ in range(N)]

# 전역변수 선언
INF = 2501
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
visited = [[False for _ in range(M)] for _ in range(N)]

# 메모이제이션
DP = [[-1 for _ in range(M)] for _ in range(N)]

# DFS(+DP)
def DFS(X, Y):
    # 탐색 불가 조건
    if X < 0 or X >= N or Y < 0 or Y >= M: return 0
    if Map[X][Y] == 'H': return 0
    if visited[X][Y]: return INF

    # 메모이제이션
    if DP[X][Y] != -1: return DP[X][Y]

    # 탐색
    result = 0
    value = Map[X][Y]
    visited[X][Y] = True
    for i in range(4):
        X_, Y_ = X+value*dx[i], Y+value*dy[i]
        result = max(result, 1+DFS(X_, Y_))
    visited[X][Y] = False # 백트래킹

    # 메모이제이션
    DP[X][Y] = result
    return result

# 함수 호출 및 출력부
result = DFS(0, 0)
print(result if result < INF else -1)