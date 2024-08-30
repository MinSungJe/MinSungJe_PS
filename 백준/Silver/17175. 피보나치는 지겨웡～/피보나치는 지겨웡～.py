# 입력부
n = int(input())

# DP 배열 선언
DP = [0 for _ in range(51)]
DP[0] = 1
DP[1] = 1

# DP 배열 채우기
for i in range(2, n+1): DP[i] = (1+DP[i-1]+DP[i-2]) % 1000000007

# 출력부
print(DP[n])