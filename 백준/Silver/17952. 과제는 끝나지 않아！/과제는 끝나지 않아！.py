# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())

# 초기값 선언
stack = deque()

# 과제 받기
result = 0
score, left = 0, 1000001
for _ in range(N):
    work = list(map(int, input().split()))
    
    # 새로운 과제를 받음
    if work[0]:
        if score and left: stack.append((score, left))
        score, left = work[1], work[2]
    
    # 과제 수행
    left -= 1

    # 과제 모두 완료
    if not left:
        result += score
        if stack: score, left = stack.pop()

# 출력부
print(result)