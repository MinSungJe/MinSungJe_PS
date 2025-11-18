# 입력부
N = int(input())

answer = 0

# 피보나치 동적 프로그래밍
DP = [0 for _ in range(N+1)]
DP[1] = 1
DP[2] = 1
for i in range(3, N+1):
    answer += 1
    DP[i] = DP[i-1] + DP[i-2]

# 출력부
print(DP[N], answer)