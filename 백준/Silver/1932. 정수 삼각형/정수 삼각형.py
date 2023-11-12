# 입력부
n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]

# DP Table
DP = [[0 for _ in range(n)] for _ in range(n)]

# Table 채우기
DP[0][0] = Map[0][0]

for i in range(1,n):
    for j in range(0,i+1):
        if j-1 < 0: DP[i][j] = DP[i-1][j] + Map[i][j]
        else: DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + Map[i][j]

print(max(DP[n-1]))