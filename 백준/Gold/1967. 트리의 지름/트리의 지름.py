# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 초기값 설정
INF = 1000001

# 입력부
n = int(input())
tree = [list() for _ in range(n+1)]
for _ in range(n-1):
    A, B, value = map(int, input().split())
    tree[A].append((value, B))
    tree[B].append((value, A))

# dijkstra
def dijkstra(start):
    heap = [(0, start)]
    result = [INF for _ in range(n+1)]
    result[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)

        if result[node] < dist: continue
        for value, next in tree[node]:
            dist_ = dist + value

            if result[next] <= dist_: continue
            result[next] = dist_
            heapq.heappush(heap, (dist_, next))
    
    # 최장거리와 해당 인덱스 구하기
    maxValue = 0
    index = 0
    for i in range(1, n+1):
        if result[i] == INF: continue
        if maxValue < result[i]:
            maxValue = result[i]
            index = i
    
    # 루트노드에서 탐색한 경우 인덱스를, 그렇지 않으면 최장거리를 return
    if start == 1: return index
    return maxValue

# 출력부
answer = dijkstra(dijkstra(1))
print(answer)