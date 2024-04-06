# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
DP = [[0 for _ in range(N)] for _ in range(N)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# DFS(+DP)
def DFS(X, Y):
    # 메모이제이션
    if DP[X][Y]: return DP[X][Y]

    # 결과값 도출
    result = 1
    for i in range(4):
        X_, Y_ = X+dx[i], Y+dy[i]
        
        # 탐색 불가 조건
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N: continue
        if Map[X][Y] >= Map[X_][Y_]: continue
        result = max(result, 1+DFS(X_, Y_))

    DP[X][Y] = result
    return result

# 결과값 도출 및 출력부
result = 1
for i in range(N):
    for j in range(N):
        result = max(result, DFS(i, j))
print(result)