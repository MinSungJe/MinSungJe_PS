# 입력부
n = int(input())
box = list(map(int, input().split()))

# 초기값 선언
DP = [1 for _ in range(n)]

# DP 배열 채우기
for i in range(1, n):
    for j in range(0, i):
        if box[j] < box[i]: DP[i] = max(DP[i], DP[j]+1)

# 출력부
print(max(DP))