# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
numlist = [int(input()) for _ in range(N)]

# 수열 정렬
numlist.sort()

# 투 포인터
lp = 0
rp = 0

result = 2000000001
while lp <= rp and rp < N:
    value = numlist[rp] - numlist[lp]

    # 조건 미충족
    if value < M: rp += 1
    else: # 조건 충족
        result = min(result, value)
        lp += 1

# 출력부
print(result)