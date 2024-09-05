# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
council = [list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간으로 정렬
council.sort(key=lambda x:(-x[1], -x[0]))

# 초기값 선언
result = 1
heap = [-council[0][1]]

# 회의실 정하기
for i in range(N):
    start, end = council[i]
    
    # 회의실을 사용할 수 있는 가장 유리한 시간(그리드)
    time = heapq.heappop(heap) * (-1)

    # 해당 시간에 회의실 사용 불가능
    if time < end:
        result += 1
        heapq.heappush(heap, -time)
    
    # 회의실을 사용할 수 있는 시간 담기
    heapq.heappush(heap, -start)

# 출력부
print(result)