# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 좋은 단어인지 찾아보는 함수
def isGood(word):
    stack = deque()
    for letter in word:
        if stack and stack[-1] == letter: stack.pop()
        else: stack.append(letter)

    if stack: return False
    else: return True


# 입력부
N = int(input())

# 함수 호출 및 결과 도출
result = 0
for _ in range(N):
    if isGood(input()): result += 1

# 출력부
print(result)