# 입력부
N = int(input())
numbers = [0] + list(map(int, input().split()))

# DP 배열 선언
DP = [[1, 1] for _ in range(N+1)]

# DP 배열 채우기
result = 1
for i in range(2, N+1):
    if numbers[i] >= numbers[i-1]: DP[i][0] = DP[i-1][0]+1
    if numbers[i] <= numbers[i-1]: DP[i][1] = DP[i-1][1]+1
    result = max(result, DP[i][0], DP[i][1])

# 출력부
print(result)