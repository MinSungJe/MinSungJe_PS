# 입력부
n = int(input())

# DP 배열 선언
INF = 100001
DP = [INF for _ in range(n+1)]
DP[0] = 0
for i in range(1, n+1):
    if i >= 2: DP[i] = min(DP[i], DP[i-2]+1)
    if i >= 5: DP[i] = min(DP[i], DP[i-5]+1)

# 출력부
answer = DP[n] if DP[n] != INF else -1
print(answer)