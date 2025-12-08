# 모듈 불러오기
import heapq

# 입력부
n = int(input())

# 초기값 선언
gifts = []


# 선물 나눠주기
for _ in range(n):
    numbers = list(map(int, input().split()))

    # 구분
    if numbers[0] == 0: # 아이를 만남
        # 출력부
        if not gifts: print(-1)
        else: print(-heapq.heappop(gifts))

    else: # 선물 충전
        gift_count, *args = numbers
        for gift_value in args: heapq.heappush(gifts, -gift_value)