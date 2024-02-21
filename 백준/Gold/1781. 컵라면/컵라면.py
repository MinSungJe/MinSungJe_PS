# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

# info 정렬
info.sort(key=lambda x:(x[0], -x[1]))

# 초기값 설정
heap = list()

# 컵라면을 돌아보며 확인
for i in range(N):
    time, value = info[i]
    if time > len(heap): heapq.heappush(heap, value)
    else:
        min_value = heapq.heappop(heap)
        heapq.heappush(heap, max(value, min_value))

# 출력부
print(sum(heap))