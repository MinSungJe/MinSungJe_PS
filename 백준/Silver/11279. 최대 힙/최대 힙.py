# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 초기값 선언
max_heap = []

# 입력부
N = int(input())
for _ in range(N):
    x = int(input())
    
    if x: # x가 0이 아니라면 튜플형태로 max_heap에 heap push
        heapq.heappush(max_heap, (-x,x)) # 0번은 key가 되고(최대값이므로 -를 붙이면 반대로 최소값) 1번은 값이 됨
    else: # x가 0이라면
        # max_heap에 값이 하나도 없는 경우
        if not max_heap: print(0)
        else: print(heapq.heappop(max_heap)[1]) # 값이 있다면 튜플 중 1번 인덱스(값) 출력