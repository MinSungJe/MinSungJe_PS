# 입력부
N = int(input())

# 초기값 선언
INF = 10000001
rest = 45678

# DP 배열 채우기
DP = [0 for _ in range(INF)]
DP[1] = 5
for i in range(2, INF): DP[i] = (DP[i-1] + (4 + 3 * (i-1)) % rest) % rest

# 출력부
answer = DP[N]
print(answer)