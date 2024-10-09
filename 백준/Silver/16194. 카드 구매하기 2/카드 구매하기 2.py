# 입력부
N = int(input())
P = [0] + list(map(int, input().split()))

# DP 배열 선언
INF = 10000001
DP = [INF for _ in range(N+1)]
DP[0] = 0
for i in range(N+1): DP[i] = P[i]

# DP 배열 채우기
for i in range(1, N+1):
    value = P[i]
    for j in range(i, N+1):
        DP[j] = min(DP[j], DP[j-i]+value)

# 출력부
print(DP[N])