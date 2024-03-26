# 입력부
N = int(input())

# DP 배열 선언
DP = [0 for _ in range(N+1)]
DP[0] = 1
DP[1] = 1

# DP 배열 채우기
for i in range(2, N+1): DP[i] = (DP[i-2]+DP[i-1]) % 15746

# 출력부
print(DP[N])