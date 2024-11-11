# 모듈 불러오기
from collections import deque

# 입력부
N, K = map(int, input().split())

# 초기값 선언
queue = deque(list(range(1, N+1)))

# 요세푸스 순열
result = []
count = 0
while queue:
    count += 1
    value = queue.popleft()
    # 빠져 나감
    if count % K == 0:
        result.append(value)
    else: # 한바퀴를 돎
        queue.append(value)

# 출력부
print(f"<{', '.join(map(str, result))}>")