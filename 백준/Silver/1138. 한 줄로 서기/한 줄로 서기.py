# 모듈 불러오기
import heapq

# 입력부
N = int(input())
line = list(map(int, input().split()))

# 초기값 선언
result = list()
graph = [list(range(i)) for i in range(N)]
heap = list()
for i in range(N):
    if not line[i]: heap.append(i)

# 위상 정렬
while heap:
    node = heapq.heappop(heap)

    # 결과 기록
    result.append(node+1)
    
    # 다음 확인
    for node_ in graph[node]:
        line[node_] -= 1
        if not line[node_]: heapq.heappush(heap, node_)

# 출력부
print(*result)