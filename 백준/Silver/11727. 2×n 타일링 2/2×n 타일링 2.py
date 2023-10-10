# 입력부
n = int(input())

# 초기 값 선언
dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 1

# dp 배열 채우기
for i in range(2,n+1):
    dp[i] = dp[i-1] + (2 * dp[i-2])

# 출력부
print(dp[n] % 10007)