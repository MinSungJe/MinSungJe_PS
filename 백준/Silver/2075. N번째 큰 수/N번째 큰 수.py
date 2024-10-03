# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())

# 초기값 선언
heap = list()

# 우선순위 큐에 값 넣기
for _ in range(N):
    numbers = list(map(int, input().split()))
    for number in numbers:
        # 힙 안 요소의 개수를 N으로 고정
        if len(heap) < N:
            heapq.heappush(heap, number)
            continue
        
        # 힙 안 최소값보다 크지 않을 경우 추가 X
        if heap[0] >= number: continue

        # 힙 요소 교체
        heapq.heappop(heap)
        heapq.heappush(heap, number)

# 출력부
result = heap[0]
print(result)