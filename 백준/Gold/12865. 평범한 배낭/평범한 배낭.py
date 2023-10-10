N, K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1,N+1):
    W, V = map(int, input().split())
    for j in range(K+1):
        dp[i][j] = dp[i-1][j]
        if j >= W: dp[i][j] = max(dp[i][j], dp[i-1][j-W]+V)
            
print(dp[N][K])