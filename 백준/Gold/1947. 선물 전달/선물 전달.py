# 입력부
N = int(input())

# DP 배열 선언
DP = [0 for _ in range(N+1)]
DP[0] = 0
DP[1] = 0
if N >= 2: DP[2] = 1

# DP 배열 채우기
for i in range(3, N+1):
    DP[i] = ((DP[i-2] + DP[i-1]) * (i-1)) % 1000000000

# 출력부
print(DP[N])