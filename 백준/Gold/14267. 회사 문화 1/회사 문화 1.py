# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n, m = map(int, input().split())

# 그래프 그리기
graph = [list() for _ in range(n+1)]
numbers = list(map(int, input().split()))
for i in range(1, n): graph[numbers[i]].append(i+1)

# 칭찬주고 결과값 도출
result = [0 for _ in range(n+1)]
for _ in range(m):
    i, w = map(int, input().split())
    result[i] += w

for i in range(1, n+1):
    for node in graph[i]: result[node] += result[i]

# 출력부
print(*result[1:])