# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 초기 값 지정
memo = {}

# 입력부
N, M = map(int, input().split())
for _ in range(N):
    site, password = input().split()
    memo[site] = password

# 출력부
for _ in range(M): print(memo[input()])