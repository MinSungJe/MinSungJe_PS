N = int(input())

dp = [-1 for _ in range(N+1)]
dp[1] = 0
if N >= 2: dp[2] = 1
if N >= 3: dp[3] = 1

def Cal(X):
    # 값이 기록된 경우 그대로 return(DP)
    if dp[X] != -1:
        return dp[X]

    # 연산 1,2 전부 해당: 6으로 나누어떨어지는 경우
    if X % 6 == 0:
        dp[X] = min(Cal(X//2), Cal(X//3)) + 1
    
    # 연산 1 해당: 3으로 나누어 떨어지는 경우
    elif X % 3 == 0:
        dp[X] = min(Cal(X//3), Cal(X-1)) + 1

    # 연산 2 해당: 2로 나누어떨어지는 경우
    elif X % 2 == 0:
        dp[X] = min(Cal(X//2), Cal(X-1)) + 1
    
    # 연산 1,2 둘다 해당하지 않음
    else:
        dp[X] = Cal(X-1) + 1

    # 계산 후 최종값 return
    return dp[X]

print(Cal(N))