# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())
last_sprayed = [-11 for _ in range(9)]

# 게임 시작
pineapples = 0
blueberries = 0
for _ in range(n):
    t, a, b = map(int, input().split())
    if a < 5 and b >= 5:
        pineapples += 100
        if t - last_sprayed[a] <= 10: pineapples += 50
        last_sprayed[a] = t
    elif a >= 5 and b < 5:
        blueberries += 100
        if t - last_sprayed[a] <= 10: blueberries += 50
        last_sprayed[a] = t

# 출력부
print(pineapples, blueberries)