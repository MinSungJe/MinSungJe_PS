# 모듈 불러오기
from collections import deque

# 입력부
n = int(input())
m = int(input())

graph = [list() for _ in range(n+1)]
enemy = [list() for _ in range(n+1)]
for _ in range(m):
    T, p, q = input().split()
    P, Q = int(p), int(q)
    if T == 'E':
        enemy[P].append(Q)
        enemy[Q].append(P)
    if T == 'F':
        graph[P].append(Q)
        graph[Q].append(P)
    
# BFS
def BFS(start):
    # 초기값 선언
    queue = deque([(start, 0)])
    visited = [False for _ in range(n+1)]

    # BFS 돌리기
    while queue:
        node, count = queue.popleft()
        # 탐색 불가 조건
        if visited[node]: continue

        
        # 친구로 연결하기
        if count == 2: graph[start].append(node)

        # 탐색
        visited[node] = True

        # 다음 탐색
        for node_ in enemy[node]: queue.append((node_, count+1))

# 추가 친구 연결하기
for idx in range(1, n+1): BFS(idx)

# union-find
P = [i for i in range(n+1)]
def find(A):
    if P[A] == A: return A
    P[A] = find(P[A])
    return P[A]

def union(A, B):
    X, Y = find(A), find(B)
    if X == Y: return
    if X < Y: P[Y] = X
    else: P[X] = Y

# 팀 찾기
for node in range(1, n+1):
    for node_ in graph[node]:
        union(node, node_)

# 출력부
answer = len(set(P[1:]))
print(answer)