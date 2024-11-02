# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
numbers = list(float(input()) for _ in range(N))

# DP
for i in range(1, N):
    numbers[i] = max(numbers[i], numbers[i]*numbers[i-1])

# 출력부
result = max(numbers)
print(f"{result:.3f}")