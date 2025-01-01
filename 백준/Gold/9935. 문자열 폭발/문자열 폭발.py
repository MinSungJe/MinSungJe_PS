# 모듈 불러오기
from collections import deque

# 폭탄이 터질 수 있는 지 확인
def checkCanBomb(bomb):
    for i in range(len(bomb)):
        if stack[len(stack)-len(bomb)+i] != bomb[i]: return False
    return True

# 입력부
letter = input()
bomb = input()

# 초기값 선언
stack = deque()

# 스택 이용 문제 해결
for l in letter:
    stack.append(l)

    # 폭탄 문자열이 있는지 확인
    while len(stack) >= len(bomb):
        if not checkCanBomb(bomb): break
        for _ in range(len(bomb)): stack.pop() # 폭발

# 출력부
result = ''.join(stack)
print(result if len(result) else 'FRULA')