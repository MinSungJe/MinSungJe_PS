# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())

# 최대힙, 최소힙 구성
maxHeap = list()
minHeap = list()

# 숫자들 입력받기
for _ in range(N):
    number = int(input())

    # 두 힙의 요소 개수가 같다면, maxHeap에 넣음
    if len(maxHeap) == len(minHeap): heapq.heappush(maxHeap, -number)
    else: heapq.heappush(minHeap, number)

    # maxHeap의 루트와 minHeap의 루트 확인 / maxHeap 루트값이 더 크다면, 둘을 바꿈
    if minHeap and -maxHeap[0] > minHeap[0]:
        maxRoot = heapq.heappop(maxHeap)
        minRoot = heapq.heappop(minHeap)
        heapq.heappush(minHeap, -maxRoot)
        heapq.heappush(maxHeap, -minRoot)

    # 출력부 (maxHeap의 루트)
    print(-maxHeap[0])