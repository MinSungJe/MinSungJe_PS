# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
DP = [[-1 for _ in range(N)] for _ in range(N)]

# DFS(+DP)
def DFS(X, Y):
    # 도착
    if X == N-1 and Y == N-1: return 1

    # 메모이제이션
    if DP[X][Y] != -1: return DP[X][Y]

    # 다음 탐색
    result = 0
    if Map[X][Y]:
        X_, Y_ = X+Map[X][Y], Y+Map[X][Y]
        if X_ < N: result += DFS(X_, Y)
        if Y_ < N: result += DFS(X, Y_)

    DP[X][Y] = result
    return result

# 함수 호출 및 출력부
result = DFS(0, 0)
print(result)