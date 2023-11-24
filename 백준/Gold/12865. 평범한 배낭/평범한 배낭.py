# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, K = map(int, input().split())

# DP Table 선언
DP = [[0 for _ in range(K+1)] for _ in range(N+1)]

# DP Table 채우기
for i in range(1, N+1):
    W, V = map(int, input().split())
    for j in range(1, K+1):
        if j < W: DP[i][j] = DP[i-1][j]
        else: DP[i][j] = max(DP[i-1][j], DP[i-1][j-W] + V)

# 출력부
print(DP[N][K])