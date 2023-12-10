# 입력부
N, M = map(int, input().split())
m = list(map(int, input().split()))
c = list(map(int, input().split()))
C = sum(c)

# DP Table 선언
DP = [[0 for _ in range(C+1)] for _ in range(N+1)]

# KnapSack
for i in range(1, N+1):
    for j in range(C+1):
        memory = m[i-1]
        cost = c[i-1]

        if j < cost: DP[i][j] = DP[i-1][j]
        else: DP[i][j] = max(DP[i-1][j], DP[i-1][j-cost]+memory)

# 출력부
result = 0
for i in range(C+1):
    if DP[N][i] >= M:
        result = i
        break
print(result)