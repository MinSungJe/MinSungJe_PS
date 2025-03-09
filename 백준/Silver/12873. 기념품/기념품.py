# 모듈 불러오기
from collections import deque

# 입력부
N = int(input())

# 초기값 선언
queue = deque(list(range(1, N+1)))
stage = 1

# queue에 한 명이 남을 때까지 반복
while len(queue) > 1:
    lose_index = ((stage**3) % len(queue)) - 1
    if lose_index < 0: lose_index += len(queue)

    for _ in range(lose_index): queue.append(queue.popleft())

    queue.popleft()
    stage += 1

# 출력부
print(queue[0])