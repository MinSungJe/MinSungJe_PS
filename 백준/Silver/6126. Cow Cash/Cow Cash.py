# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
V, N = map(int, input().split())
coins = [int(input()) for _ in range(V)]

# DP 배열 선언
DP = [0 for _ in range(N+1)]

# DP 배열 채우기
for coin in coins:
    if coin > N: continue
    DP[coin] += 1
    for idx in range(coin, N+1):
        if idx - coin <= 0: continue
        DP[idx] += DP[idx-coin]

# 출력부
print(DP[N])