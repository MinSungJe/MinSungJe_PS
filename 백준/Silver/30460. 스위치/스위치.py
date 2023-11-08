# 입력부
N = int(input())
A = list(map(int, input().split()))

# DP table 선언
MIN = -200000001
DP = [[MIN,MIN,MIN,MIN] for _ in range(N)]
DP[0][0] = A[0]
DP[0][3] = 2 * A[0]

# DP table 채우기
for i in range(1,N):
    DP[i][0] = max(DP[i-1][0], DP[i-1][1]) + A[i]
    if i >= 2: DP[i][1] = DP[i-1][2] + 2 * A[i]
    DP[i][2] = DP[i-1][3] + 2 * A[i]
    DP[i][3] = max(DP[i-1][0], DP[i-1][1]) + 2 * A[i]

# 출력부
print(max(DP[N-1]))