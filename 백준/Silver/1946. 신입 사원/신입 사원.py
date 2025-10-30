# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
T = int(input())
for _ in range(T):
    N = int(input())
    applies = [list(map(int, input().split())) for _ in range(N)]

    # 서류심사 순으로 정렬
    applies.sort()

    # 모노톤 스택
    stack = deque()
    for _, score in applies:
        if len(stack) != 0 and stack[-1] < score: continue
        stack.append(score)

    # 결론 도출 및 출력부
    answer = len(stack)
    print(answer)