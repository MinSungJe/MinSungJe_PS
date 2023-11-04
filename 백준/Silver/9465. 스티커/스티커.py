# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# TC
T = int(input())
for test_case in range(T):
    # 입력부
    n = int(input())
    top = [0] + list(map(int, input().split()))
    bottom = [0] + list(map(int, input().split()))

    # 초기값 선언
    dp = [[0,0] for _ in range(n+1)]

    # dp배열 채우기
    dp[1][0] = top[1]
    dp[1][1] = bottom[1]
    for i in range(2,n+1):
        dp[i][0] = max(dp[i-1][1], dp[i-2][1]) + top[i]
        dp[i][1] = max(dp[i-1][0], dp[i-2][0]) + bottom[i]

    print(max(dp[n]))