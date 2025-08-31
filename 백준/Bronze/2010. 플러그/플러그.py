import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
answer = 0
for _ in range(N): answer += int(input()) - 1
print(answer+1)