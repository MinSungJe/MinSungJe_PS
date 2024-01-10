# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())

# 그래프 입력
graph = [list() for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

# 밸만포드 알고리즘
INF = 5000001
result = [INF for _ in range(N+1)]
result[1] = 0 # 출발노드: 1
isCycle = False

for _ in range(N-1): # (노드의 개수-1)만큼 반복
    for node in range(1, N+1): # 모든 노드에 있는
        if result[node] == INF: continue
        for node_, value in graph[node]: # 모든 간선에 대해 탐색
            result[node_] = min(result[node_], result[node]+value)

# 마지막으로 한번 더 확인
for node in range(1, N+1): # 모든 노드에 있는
    if result[node] == INF: continue
    for node_, value in graph[node]: # 모든 간선에 대해 탐색
        if result[node_] != min(result[node_], result[node]+value): # 만약 값이 갱신됐다면, 음의 순환이 있음
            isCycle = True
            break
    if isCycle: break

# 출력부
if isCycle: print(-1)
else:
    for i in range(2, N+1): print(result[i] if result[i] < INF else -1)