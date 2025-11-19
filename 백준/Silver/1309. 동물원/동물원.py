# 입력부
N = int(input())

# 초기값 선언
rest = 9901

# DP 배열 선언
DP = [[0, 0, 0] for _ in range(N+1)]
DP[0][0] = 1

# DP 배열 채우기
for i in range(1, N+1):
    DP[i][0] = (DP[i-1][0] + DP[i-1][1] + DP[i-1][2]) % rest
    DP[i][1] = (DP[i-1][0] + DP[i-1][2]) % rest
    DP[i][2] = (DP[i-1][0] + DP[i-1][1]) % rest

# 출력부
answer = sum(DP[N]) % rest
print(answer)