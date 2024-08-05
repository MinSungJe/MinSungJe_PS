# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
homework = [list(map(int, input().split())) for _ in range(N)]

# 마감일 순으로 과제 정리
homework.sort(key=lambda x: (x[0], -x[1]))

# 끝낼 과제 넣을 heap 제작
heap = list()
for d, w in homework:
    # 과제 할거라고 예약
    heapq.heappush(heap, w)

    # 기한이 넘어간 경우 가장 적은 점수의 과제 제거
    if d < len(heap): heapq.heappop(heap)

# 출력부
result = sum(heap)
print(result)