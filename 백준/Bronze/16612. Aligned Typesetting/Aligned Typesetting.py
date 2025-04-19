# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n, L = map(int, input().split())
words = [input() for _ in range(n)]

# 가능 여부 계산
for word in words: L -= len(word)
result = False
if n == 1:
    if L == 0: result = True
else:
    if L > 0 and not L % (n-1): result = True

# 출력부
print('Yes' if result else 'No')