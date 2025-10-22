# 모듈 불러오기
from collections import deque

# 입력부
N, M, X = map(int, input().split())

# 그래프 그리기
up_graph = [list() for _ in range(N+1)]
down_graph = [list() for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    up_graph[A].append(B)
    down_graph[B].append(A)

# 방문된 노드 찾기
def BFS(start, graph):
    # 초기값 선언
    visited = [0 for _ in range(N+1)]
    queue = deque([(start)])

    # 탐색
    while queue:
        node = queue.popleft()
        
        # 탐색 불가 조건
        if visited[node]: continue

        # 탐색
        visited[node] = 1

        # 다음 탐색
        for node_ in graph[node]: queue.append(node_)
    
    # 방문한 노드 개수 계산
    result = sum(visited)
    return result

# 나보다 더 못한 사람, 더 잘한 사람 계산
worse = BFS(X, up_graph) - 1
better = BFS(X, down_graph) - 1

# 최대, 최소 등수 계산
highest = 1 + better
lowest = N - worse

# 출력부
print(highest, lowest)