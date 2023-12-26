# 입력부
N = int(input())
Map = list(map(int, input().split()))

# DP Table 선언
DP = [0 for _ in range(N)]

# DP Table 채우기
DP[0] = 1
for i in range(1, N):
    max_value = 0
    idx = -1
    for j in range(i):
        if Map[j] > Map[i] and max_value < DP[j]:
            idx = j
            max_value = DP[j]
    if idx != -1: DP[i] = DP[idx] + 1
    else: DP[i] = 1

# 출력부
print(N-max(DP))