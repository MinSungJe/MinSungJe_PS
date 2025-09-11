# 모듈 불러오기
from collections import deque

# 입력부
N = int(input())
buildings = [int(input()) for _ in range(N)]

# 초기값 선언
stack = deque()

# 값 구하기
answer = 0
for building in buildings:
    # 모노톤 스택
    while stack and stack[-1] <= building: stack.pop()

    # 자신을 볼 수 있는 건물의 수 더하기
    answer += len(stack)

    # 스택에 값 추가
    stack.append(building)

# 출력부
print(answer)