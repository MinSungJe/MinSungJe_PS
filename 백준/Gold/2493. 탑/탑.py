# 모듈 불러오기
from collections import deque

# 입력부
N = int(input())
tower = list(map(int, input().split()))

# 초기값 선언
stack = deque()
result = [0 for _ in range(N)]

# 스택 이용 값 구하기
for i in range(N):
    while stack:
        idx, tall = stack.pop() # 스택에서 값 확인
        if tall > tower[i]: # 신호를 받음
            result[i] = idx
            stack.append((idx, tall))
            stack.append((i+1, tower[i]))
            break
    
    if not stack: # 스택이 비어있는 경우
        result[i] = 0
        stack.append((i+1, tower[i]))

# 출력부
print(*result)