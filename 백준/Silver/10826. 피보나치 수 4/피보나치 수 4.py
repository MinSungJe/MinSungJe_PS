# 입력부
N = int(input())

# 피보나치 배열 기록
DP = [0 for _ in range(10001)]
DP[1] = 1
for i in range(2, 10001): DP[i] = DP[i-1] + DP[i-2]

# 출력부
print(DP[N])