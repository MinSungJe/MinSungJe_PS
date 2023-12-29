# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n, k = map(int, input().split())
coins = list()
for _ in range(n): coins.append(int(input()))

# DP Table 채우기 (Bottom-Up)
DP = [0 for _ in range(k+1)]
DP[0] = 1
for coin in coins:
    for i in range(coin, k+1): DP[i] += DP[i-coin]

# 출력부
print(DP[k])