# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, K = map(int, input().split())
# 하나의 리스트에 보석, 가방(checkpoint)을 기록
arr = [tuple(map(int, input().split())) for _ in range(N)]
INF = 100000001
for _ in range(K): arr.append((int(input()), INF))
arr.sort()

# 초기값 선언
result = 0
heap = []

# 리스트 돌며 확인
for weight, value in arr:
    # 가방이 아니라면, heap에 넣기
    if value != INF: heapq.heappush(heap, -value)
    # 가방이라면, heap에서 가장 큰 value를 꺼내 결과값에 더하기
    else:
        if heap: result -= heapq.heappop(heap)

# 출력부
print(result)