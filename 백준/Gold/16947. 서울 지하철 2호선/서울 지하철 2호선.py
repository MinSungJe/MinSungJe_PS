# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
graph = [list() for _ in range(N+1)]
for _ in range(N):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# DFS 돌리는 함수
def DFS(node):
    # 초기값 선언
    result = 0
    visited = [-1 for _ in range(N+1)]
    queue = deque([(node, 0)])

    # DFS
    while queue:
        idx, count = queue.pop()

        # 탐색 종료 조건
        if visited[idx] != -1:
            if count == visited[idx]+2: continue
            result = visited[idx]
            break

        # 탐색
        visited[idx] = count

        # 다음 탐색
        for idx_ in graph[idx]:
            queue.append((idx_, count+1))
    
    return result

# 함수 호출
result = list(map(DFS, list(range(1, N+1))))
print(*result)