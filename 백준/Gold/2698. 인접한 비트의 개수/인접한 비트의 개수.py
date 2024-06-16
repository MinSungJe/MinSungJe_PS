# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# DP 배열 선언
DP = [[[0, 0] for _ in range(101)] for _ in range(101)]

# 배열 채우기
DP[1][0][0] = 1
DP[1][0][1] = 1
for i in range(2, 101):
    for j in range(0, i):
        for k in range(2):
            if k == 0:
                DP[i][j][k] += DP[i-1][j][0]
                DP[i][j][k] += DP[i-1][j][1]
            else:
                DP[i][j][k] += DP[i-1][j][0]
                DP[i][j][k] += DP[i-1][j-1][1]

# 입력부 및 출력부
T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    result = sum(DP[n][k])
    print(result)