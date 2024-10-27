# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
sell = dict()
for _ in range(N):
    book = input()
    if not sell.get(book): sell[book] = 1
    else: sell[book] += 1

# 가장 많이 팔린 책 구하기
result = []
max_value = max(sell.values())
for k in sell.keys():
    if sell[k] == max_value: result.append(k)
result.sort()

# 출력부
print(result[0])