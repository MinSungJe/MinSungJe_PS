# 모듈 불러오기
from collections import deque

# 입력부
N, K = map(int, input().split())
numbers = list(map(int, list(input())))

# 초기값 설정
stack = deque()

# 값 하나씩 넣어보며 확인(모노톤 스택)
for i in range(N):
    while stack and K and stack[-1] < numbers[i]:
        stack.pop()
        K -= 1
    stack.append(numbers[i])

# 빠지지 않은 수 뒤에서 빼기
while K:
    stack.pop()
    K -= 1

# 출력부
print(''.join(map(str, stack)))