# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
lecture = [list(map(int, input().split())) for _ in range(N)]
lecture.sort(key=lambda x:x[1])

# 초기값 선언
heap = [lecture[0][2]]

# 모든 강의를 확인
for i in range(1, N):
    last_time = heapq.heappop(heap)
    if lecture[i][1] < last_time:
        heapq.heappush(heap, last_time)
    heapq.heappush(heap, lecture[i][2])

# 출력부
print(len(heap))