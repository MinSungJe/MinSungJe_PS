# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())

value = [0 for _ in range(N+1)]
graph = [list() for _ in range(N+1)]
phase = [0 for _ in range(N+1)]
result = [0 for _ in range(N+1)]

for i in range(1, N+1):
    info = list(map(int, input().split()))
    value[i] = info[0]
    for node in info[1:-1]:
        graph[node].append(i)
        phase[i] += 1

# 위상이 0인 노드부터 넣기
heap = list()
for i in range(1, N+1):
    if phase[i] == 0: heapq.heappush(heap, (0, i))

# 위상정렬 알고리즘
while heap:
    time, node = heapq.heappop(heap)

    time = max(time, result[node]) # 저장된 값이 있는지 확인
    result[node] = time + value[node]

    # 다음 탐색
    for node_ in graph[node]:
        phase[node_] -= 1
        result[node_] = max(result[node_], result[node]) # 도착할 위치에 미리 저장
        if phase[node_] == 0: heapq.heappush(heap, (result[node], node_))

# 출력부
for i in range(1, N+1): print(result[i])