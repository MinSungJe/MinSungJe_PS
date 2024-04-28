# 모듈 불러오기
from collections import deque

# 입력부
N = int(input())
A = list(map(int, input().split()))

# 초기값 선언
stack = deque()
result = [0 for _ in range(N)]

# 결과값 채우기
for i in range(N-1, -1, -1):
    if stack:
        while stack:
            value = stack.pop()
            if A[i] < value:
                result[i] = value
                stack.append(value)
                break
        
    if not stack: result[i] = -1
    
    stack.append(A[i])

# 출력부
print(*result)