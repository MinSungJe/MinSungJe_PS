# 모듈 불러오기
from collections import deque

# 입력부
N = int(input())
A = list(map(int, input().split()))

# 초기값 선언
result = deque()

# 뒤에서부터 확인
for i in range(N-1, -1, -1):
    cmd = A[i]
    value = N-i
    if cmd == 1: result.appendleft(value)
    if cmd == 2:
        top = result.popleft()
        result.appendleft(value)
        result.appendleft(top)
    if cmd == 3: result.append(value)

# 출력부
print(*result)