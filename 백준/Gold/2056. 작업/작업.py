# 빠른 입력
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())

# 초기값 선언
result = 0
heap = list()
phase = [0 for _ in range(N+1)]
time = [0 for _ in range(N+1)]
graph = [list() for _ in range(N+1)]

# 그래프 그리기
for i in range(1, N+1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    if info[1] == 0:
        heapq.heappush(heap, (info[0], i))
        continue
    phase[i] = info[1]
    
    for node in info[2:]:
        graph[node].append(i)

# 위상 정렬
while heap:
    value, node = heapq.heappop(heap)

    # 다음 탐색
    result = max(result, value)
    for node_ in graph[node]:
        phase[node_] -= 1
        if phase[node_] == 0: heapq.heappush(heap, (value+time[node_], node_))

# 출력부
print(result)