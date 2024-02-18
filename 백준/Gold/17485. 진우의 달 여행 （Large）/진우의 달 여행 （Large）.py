# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
INF = 100001

# DP 배열 선언
DP = [[[0 for _ in range(3)] for _ in range(M)] for _ in range(N)]
for i in range(M):
    for j in range(3):
        DP[0][i][j] = Map[0][i]
DP[0][0][0] = INF
DP[0][M-1][2] = INF

# Bottom-Up
for i in range(1, N):
    for j in range(M):
        if j == 0:
            for k in range(3):
                if k == 0: DP[i][j][k] = INF
                if k == 1: DP[i][j][k] = Map[i][j] + min(DP[i-1][j][0], DP[i-1][j][2])
                if k == 2: DP[i][j][k] = Map[i][j] + min(DP[i-1][j+1][0], DP[i-1][j+1][1])
        elif j == M-1:
            for k in range(3):
                if k == 0: DP[i][j][k] = Map[i][j] + min(DP[i-1][j-1][1], DP[i-1][j-1][2])
                if k == 1: DP[i][j][k] = Map[i][j] + min(DP[i-1][j][0], DP[i-1][j][2])
                if k == 2: DP[i][j][k] = INF
        else:
            for k in range(3):
                if k == 0: DP[i][j][k] = Map[i][j] + min(DP[i-1][j-1][1], DP[i-1][j-1][2])
                if k == 1: DP[i][j][k] = Map[i][j] + min(DP[i-1][j][0], DP[i-1][j][2])
                if k == 2: DP[i][j][k] = Map[i][j] + min(DP[i-1][j+1][0], DP[i-1][j+1][1])

# 결과값 계산 및 출력부
result = INF
for j in range(M):
    for k in range(3): result = min(result, DP[N-1][j][k])
print(result)