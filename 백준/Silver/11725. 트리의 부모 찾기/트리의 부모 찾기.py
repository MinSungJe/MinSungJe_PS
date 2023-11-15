# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
tree = [list() for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

# 초기값 선언
result = [0 for _ in range(N+1)]
result[1] = 1
queue = deque([1])

# BFS
while queue:
    node = queue.popleft()

    # 다음 탐색
    for next in tree[node]:
        if result[next]: continue
        else: result[next] = node
        queue.append(next)

# 출력부
for ans in result[2:]:
    print(ans)