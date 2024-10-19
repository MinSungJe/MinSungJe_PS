# 입력부
n = int(input())

# DP 배열 선언
DP = [0 for _ in range(n+1)]
DP[1] = 1
if n >= 2: DP[2] = 2

# DP 배열 채우기
for i in range(3, n+1): DP[i] = (DP[i-1] + DP[i-2]) % 10

# 출력부
result = DP[n]
print(result)