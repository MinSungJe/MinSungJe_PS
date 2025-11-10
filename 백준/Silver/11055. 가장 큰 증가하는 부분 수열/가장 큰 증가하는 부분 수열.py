# 입력부
N = int(input())
A = list(map(int, input().split()))
A = [0] + A

# DP 배열 선언
DP = [0 for _ in range(N+1)]

# DP 배열 채우기
for i in range(1, N+1):
    for j in range(i):
        if A[j] >= A[i]: continue
        DP[i] = max(DP[i], DP[j]+A[i])

# 출력부
answer = max(DP)
print(answer)