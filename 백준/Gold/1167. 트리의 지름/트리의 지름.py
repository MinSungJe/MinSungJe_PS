# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
V = int(input())
tree = [list() for _ in range(V+1)]
for _ in range(V):
    inputs = list(map(int, input().split()))
    for i in range(1, len(inputs)-1):
        if i % 2 != 0: tree[inputs[0]].append((inputs[i+1] ,inputs[i]))

# 초기값 선언
INF = 1000000001

# 다익스트라
def dijkstra(start):
    result = [INF for _ in range(V+1)]
    result[start] = 0

    heap = [(0, start)]
    while heap:
        dist, node = heapq.heappop(heap)
        if dist > result[node]: continue

        for value, next in tree[node]:
            dist_ = dist + value
            if dist_ >= result[next]: continue
            result[next] = dist_
            heapq.heappush(heap, (dist_, next))

    # 최장거리의 값과 해당 인덱스를 계산
    maxValue = 0
    idx = 0
    for i in range(1,V+1):
        if result[i] == INF: continue
        if result[i] > maxValue:
            maxValue = result[i]
            idx = i
    
    # 출발 노드에 따라 최장거리 값 또는 인덱스 return
    if start == 1: return idx
    return maxValue

# 출력부
print(dijkstra(dijkstra(1)))