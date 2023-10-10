# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())

# 초기 변수 선언
heap = []

# 출력부
for _ in range(N):
    x = int(input())
    if not x:
        if not heap: print(0)
        else: print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)