# 입력부
N = int(input())
dp = [[0,0] for _ in range(N+1)]
stair = list(int(input()) for _ in range(N))
stair = [0] + stair # Captioning

# 초기값 설정
dp[1][0] = stair[1]
if N >= 2:
    dp[2][0] = dp[1][0] + stair[2]
    dp[2][1] = stair[2]

# dp 채우기
for i in range(3,N+1):
    dp[i][0] = dp[i-1][1] + stair[i]
    dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + stair[i]

print(max(dp[N]))