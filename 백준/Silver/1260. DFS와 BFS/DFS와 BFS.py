from collections import deque

N, M, V = map(int, input().split())

# 변수 선언
edge = [[] for _ in range(N+1)]
dfsResult = []
bfsResult = []

# 그래프 입력부
for _ in range(M):
    A, B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)

# DFS: stack 이용
stack = deque()
stack.append(V)
visited = [False for _ in range(N+1)]

while stack:
    # stack에서 현재 숫자를 꺼냄
    idx = stack.pop()

    # 이미 방문한 경우, continue
    if visited[idx]: continue

    # 방문 성공, 방문했다는 표시 이후 result에 결과 집어넣음
    visited[idx] = True
    dfsResult.append(idx)

    # 다음 방문할 정점을 stack에 집어넣음
    for i in sorted(edge[idx], reverse = True):
        stack.append(i)

print(*dfsResult)

# BFS: queue 이용
queue = deque()
queue.append(V)
visited = [False for _ in range(N+1)]

while queue:
    # queue에서 현재 숫자를 꺼냄
    idx = queue.popleft()

    # 이미 방문한 경우, continue
    if visited[idx]: continue

    # 방문 성공, 방문했다는 표시 이후 result에 결과 집어넣음
    visited[idx] = True
    bfsResult.append(idx)

    # 다음 방문할 정점을 queue에 집어넣음
    for i in sorted(edge[idx]):
        queue.append(i)

print(*bfsResult)