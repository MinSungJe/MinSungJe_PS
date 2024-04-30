# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
INF = 2**31
DP = [[INF if i != j else 0 for j in range(N)] for i in range(N)]

# DP 배열 채우기
for d in range(1, N):
    for i in range(N):
        j = i+d
        if j >= N: continue

        for k in range(i, j):
            DP[i][j] = min(DP[i][j], DP[i][k] + DP[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])

# 출력부
print(DP[0][N-1])