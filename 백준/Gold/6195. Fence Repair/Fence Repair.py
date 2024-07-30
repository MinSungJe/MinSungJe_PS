# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
planks = [int(input()) for _ in range(N)]

# 정렬(힙 만들기)
planks.sort()

# 비용 계산
result = 0
while len(planks) > 1:
    # 짧은 토막 두 개 가져오기
    A = heapq.heappop(planks)
    B = heapq.heappop(planks)

    # 결과에 합치기
    value = A+B
    result += value
    heapq.heappush(planks, value)

# 출력부
print(result)