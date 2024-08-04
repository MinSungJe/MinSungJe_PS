# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]

# 강의 정렬
lectures.sort(key=lambda x:(x[1], -x[0]))

# 강의목록에서 heap으로 강의 옮기기
heap = list()
for lecture in lectures:
    p, d = lecture
    heapq.heappush(heap, p)

    # 강의를 넣을 수 없는 경우 가장 작은 강의 제거
    if len(heap) > d: heapq.heappop(heap)

# 출력부
result = sum(heap)
print(result)