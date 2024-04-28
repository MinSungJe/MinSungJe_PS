# 모듈 불러오기
from collections import deque

# 입력부
N = int(input())
A = list(map(int, input().split()))

# 초기값 선언
stack = deque()
result = [-1 for _ in range(N)]

# 결과값 채우기
for i in range(N):
    while stack and A[stack[-1]] < A[i]: # 모노톤 스택
        result[stack.pop()] = A[i]
    stack.append(i)

# 출력부
print(*result)