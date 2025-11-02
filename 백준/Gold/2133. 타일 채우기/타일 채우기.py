# 입력부
N = int(input())

# DP 배열 선언
DP = [0 for _ in range(31)]
DP[0] = 1
DP[1] = 0
for i in range(2, 31, 2):
    DP[i] += DP[i-2] * 3
    for j in range(0, i-2, 2):
        DP[i] += DP[j] * 2

# 결과 도출 및 출력부
answer = DP[N]
print(answer)