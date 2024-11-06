# 입력부
n = int(input())
numbers = list(map(int, input().split()))

# DP 배열 선언
INF = 1001
DP = [-INF for _ in range(n)]
DP[0] = numbers[0]

# DP 배열 채우기
for i in range(1, n): DP[i] = max(numbers[i], DP[i-1]+numbers[i])

# 출력부
result = max(DP)
print(result)