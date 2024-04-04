# 모듈 불러오기
from collections import deque

# 입력부
stack = deque(list(input()))

# 초기값 선언
temp = deque()

# 스택값 빼면서 확인
while stack:
    temp.append(stack.popleft())

    # temp 맨 마지막이 PPAP인지 확인
    if len(temp) >= 4:
        if temp[-1] != 'P': continue
        if temp[-2] != 'A': continue
        if temp[-3] != 'P': continue
        if temp[-4] != 'P': continue
        for _ in range(4): temp.pop()
        stack.appendleft('P')

# 출력부
print("PPAP" if len(temp) == 1 and temp[0] == 'P' else "NP")