# 입력부
N, M = map(int, input().split())
heavy_graph = [list() for _ in range(N+1)]
light_graph = [list() for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    heavy_graph[a].append(b)
    light_graph[b].append(a)

# DFS
def DFS(node, Map):
    # 탐색 불가 조건
    if visited[node]: return 0

    # 탐색
    visited[node] = True
    
    # 다음 탐색
    result = 0
    for node_ in Map[node]:
        if not visited[node_]: result += 1 
        result += DFS(node_, Map)

    return result

# 자신보다 무거운 구슬 결과 얻기
heavy_answer = [0 for _ in range(N+1)]
for start in range(1, N+1):
    visited = [False for _ in range(N+1)]
    heavy_answer[start] = DFS(start, heavy_graph)

# 자신보다 가벼운 구슬 결과 얻기
light_answer = [0 for _ in range(N+1)]
for start in range(1, N+1):
    visited = [False for _ in range(N+1)]
    light_answer[start] = DFS(start, light_graph)

# 중간이 될 수 없는 구슬 찾기
cant_middle_marble = set()
for i in range(1, N+1):
    if heavy_answer[i] >= (N+1)//2: cant_middle_marble.add(i)
    if light_answer[i] >= (N+1)//2: cant_middle_marble.add(i)

# 출력부
answer = len(cant_middle_marble)
print(answer)