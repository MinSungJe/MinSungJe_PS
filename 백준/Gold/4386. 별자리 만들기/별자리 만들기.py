# 빠른 입력
import sys, math, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]

# 그래프 만들기
graph = [list() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: continue
        value = round(math.sqrt(((stars[i][0]-stars[j][0]) ** 2)+((stars[i][1]-stars[j][1]) ** 2)), 2)
        graph[i].append((value, j))

# 초기값 설정

# 프림 알고리즘
def Prim(start):
    # 초기값 설정
    result = 0
    heap = []
    visited = [False for _ in range(n)]

    # 시작노드에서 다음 간선들 정보 넣기
    visited[start] = True
    for info in graph[start]:
        heapq.heappush(heap, info)
    
    # 우선순위 큐를 돌며 실행
    while heap:
        dist, node = heapq.heappop(heap)

        # 탐색 불가 조건
        if visited[node]: continue

        # 별자리 잇기
        result += dist
        visited[node] = True

        # 다음 값 넣기
        for info in graph[node]:
            heapq.heappush(heap, info)
    
    return result

# 출력부
print(Prim(0))