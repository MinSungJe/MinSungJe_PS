# 입력부
N = int(input())
A = [1001] + list(map(int, input().split()))
result = 1

# DP Table 선언
DP = [[0,0] for _ in range(N+1)]
DP[1][0] = 1
DP[1][1] = 1

# DP Table 채우기
for i in range(2,N+1):
    for j in range(1, i):
        if A[j] < A[i]:
            DP[i][0] = max(DP[j][0], DP[i][0])
    for j in range(1, i):
        if A[j] > A[i]:
            DP[i][1] = max(max(DP[j][0], DP[j][1]), DP[i][1])
    DP[i][0] += 1
    DP[i][1] += 1

    result = max(result, DP[i][0], DP[i][1])

# 출력부
print(result)