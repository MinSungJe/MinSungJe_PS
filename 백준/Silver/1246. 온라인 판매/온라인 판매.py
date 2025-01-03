# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
P = list(int(input()) for _ in range(M))

# 주어진 가격에서 수익을 구하는 함수
def getEarning(price):
    value = 0
    for i in range(M):
        if P[i] >= price: value += price

    return min(value, price*min(N, M))

# 계란 가격 제시
prices = list(set(P))
prices.sort(reverse=True)

# 주어진 가격의 수익 구하기
min_price = 1000001
max_earning = 0
for price in prices:
    earning = getEarning(price)
    if max_earning <= earning:
        min_price, max_earning = price, earning

# 출력부
print(min_price, max_earning)