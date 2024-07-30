# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# TC
T = int(input())
for test_case in range(1, T+1):
    K = int(input())
    page = list(map(int, input().split()))

    # 정렬
    page.sort()

    # 페이지 합치기
    result = 0
    while len(page) > 1:
        A = heapq.heappop(page)
        B = heapq.heappop(page)
        cost = A+B
        result += cost # 비용 더해두기
        heapq.heappush(page, cost) # 새로운 페이지 추가

    # 출력부
    print(result)