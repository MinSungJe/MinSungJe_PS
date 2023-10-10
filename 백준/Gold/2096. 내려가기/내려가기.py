# 입력부
N = int(input())

L, M, R = map(int, input().split())
# DP배열 선언
dp = [L, M, R, L, M, R]

# 값을 입력받으면서 바로 배열에 저장
for i in range(N-1):
    L, M, R = map(int, input().split())
    tmp = dp[:]
    dp[0] = max(tmp[0], tmp[1]) + L
    dp[1] = max(tmp[0], tmp[1], tmp[2]) + M
    dp[2] = max(tmp[1], tmp[2]) + R
    dp[3] = min(tmp[3], tmp[4]) + L
    dp[4] = min(tmp[3], tmp[4], tmp[5]) + M
    dp[5] = min(tmp[4], tmp[5]) + R

# 출력부
print(max(dp[0:3]), min(dp[3:6]))