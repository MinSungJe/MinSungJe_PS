# 모듈 불러오기
from collections import deque

# 입력부
N = int(input())

# 초기값 선언
result = list()
queue = deque(list(range(1, N+1)))

# 행동 반복
while len(queue) > 1:
    result.append(str(queue.popleft()))
    queue.append(queue.popleft())

# 출력부
print(f"{' '.join(result)} {queue[0]}" if N > 1 else queue[0])