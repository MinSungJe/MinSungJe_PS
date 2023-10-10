# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
noSee = [input() for _ in range(N)]
noHear = [input() for _ in range(M)]

# 듣도보도 못한 사람 찾기
noSeeHear = list(set(noSee).intersection(set(noHear)))
noSeeHear.sort()

# 출력부
print(len(noSeeHear))
for i in range(len(noSeeHear)): print(noSeeHear[i])