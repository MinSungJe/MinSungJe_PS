# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
numlist = list(map(int, input().split()))

# 인덱스를 담은 딕셔너리 생성
Keys = sorted(set(numlist))
idx = {}
for i,j in enumerate(Keys):
    idx[j] = i

# 출력부
result = []
for i in numlist:
    result.append(idx[i])

print(*result)