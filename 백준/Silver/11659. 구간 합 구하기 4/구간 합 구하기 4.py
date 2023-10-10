# 빠른 입출력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
numlist = list(map(int, input().split()))

# 초기값 선언
Sum = 0
Sums = [0 for _ in range(N+1)]
for i in range(1,N+1):
    Sum += numlist[i-1]
    Sums[i] = Sum

# 입력 및 출력부
for test_case in range(M):
    start, end = map(int, input().split())
    print(Sums[end]-Sums[start-1])