# 입력부
N = int(input())

# DP 배열 선언
DP = [[0 for _ in range(2)] for _ in range(N+1)]
DP[0][1] = 1

# DP 배열 채우기
for i in range(1, N+1):
    DP[i][0] = DP[i-1][0] + DP[i-1][1]
    DP[i][1] = DP[i-1][0]

# 결과 도출 및 출력부
answer = max(DP[N])
print(answer)