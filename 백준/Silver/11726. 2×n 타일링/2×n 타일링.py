# 입력부
n = int(input())

# 초기 값 선언
dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 1

# dp배열 채우기
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]

# 결과값 출력
print(dp[n]%10007)