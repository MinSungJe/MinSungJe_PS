# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())
drinks = [0] + list(int(input()) for _ in range(n))

# DP 배열 선언
DP = [-1 for _ in range(n+1)]
DP[0] = 0
DP[1] = drinks[1]
if n >= 2: DP[2] = drinks[1]+drinks[2]

# DP 배열 채우기
for i in range(3, n+1):
    DP[i] = max(DP[i-3]+drinks[i-1]+drinks[i], DP[i-2]+drinks[i], DP[i-1])

# 출력부
print(DP[n])