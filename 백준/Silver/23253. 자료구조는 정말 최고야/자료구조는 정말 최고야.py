# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque

# 입력부
N, M = map(int, input().split())

# 책 정렬 여부 확인
result = 'Yes'
for i in range(M):
    k = int(input())
    stack = deque(list(map(int, input().split())))

    # 스택에서 값을 빼가며 정렬 여부 확인
    last_value = 0
    while stack:
        value = stack.pop()
        if value < last_value:
            result = 'No'
            break
        last_value = value

    if result == 'No': break

# 출력부
print(result)