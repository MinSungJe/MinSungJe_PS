# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

# DP 배열 선언
DP = [0 for _ in range(N+1)]

# DP 배열 채우기
max_value = 0
for i in range(N-1, -1, -1):
    index = i + table[i][0]
    if index <= N: max_value = max(max_value, DP[index] + table[i][1])
    DP[i] = max_value

# 출력부
print(max_value)