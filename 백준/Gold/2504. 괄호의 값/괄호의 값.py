# 모듈 불러오기
from collections import deque

# 입력부
letter = input()

# 초기값 선언
stack = deque()
answer = 0
temp = 1
prev_open = False

# 괄호 확인
for bracket in letter:
    if bracket == '(':
        stack.append(bracket)
        temp *= 2
        prev_open = True

    if bracket == ')':
        if len(stack) == 0 or stack.pop() != '(':
            answer = 0
            break

        if prev_open == True: answer += temp
        temp //= 2
        prev_open = False

    if bracket == '[':
        stack.append(bracket)
        temp *= 3
        prev_open = True

    if bracket == ']':
        if len(stack) == 0 or stack.pop() != '[':
            answer = 0
            break

        if prev_open == True: answer += temp
        temp //= 3
        prev_open = False

# 스택에 값이 남음
if len(stack) != 0: answer = 0

# 출력부
print(answer)