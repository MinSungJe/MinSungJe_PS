# 입력부
N = int(input())

# 초기값 선언
DP = [0 for _ in range(N+1)]
if N >= 1: DP[1] = 1

for i in range(2, N+1): DP[i] = (DP[i-1] + DP[i-2]) % 1000000007

# 출력부
answer = DP[N]
print(answer)