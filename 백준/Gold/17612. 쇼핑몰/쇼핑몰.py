# 빠른 입력
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, k = map(int, input().split())

# 초기값 선언
casher = [list() for _ in range(k)]
casher_idx = 0
wait, done = list(), list()

# 손님 받기
for _ in range(N):
    value, w = map(int, input().split())

    # 빈 계산대가 있는 경우
    if casher_idx < k:
        heapq.heappush(wait, (w, casher_idx, value))
        casher_idx += 1
        continue

    # 적절한 계산대 찾기
    time, idx, prev_value = heapq.heappop(wait)
    heapq.heappush(done, (time, -idx, prev_value)) # 완료손님으로 넣기
    heapq.heappush(wait, (time+w, idx, value)) # 새 손님 계산대에 두기

# 남은 손님 모두 계산하기
while wait:
    time, idx, prev_value = heapq.heappop(wait)
    heapq.heappush(done, (time, -idx, prev_value))


# 결과 도출
result = 0
multiply = 1
while done:
    _, _, value = heapq.heappop(done)
    result += value * multiply
    multiply += 1

# 출력부
print(result)