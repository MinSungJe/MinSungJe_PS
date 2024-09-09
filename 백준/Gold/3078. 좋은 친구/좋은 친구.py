# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, K = map(int, input().split())
friends = [len(input()) for _ in range(N)]

# 초기값 선언
result = 0
queue = deque()
count = [-1 for _ in range(21)]

for value in friends:
    # 큐에 값 넣기
    queue.append(value)
    count[value] += 1

    # 가장 오래된 값 내쫒기
    if len(queue) > K+1:
        temp = queue.popleft()
        count[temp] -= 1

    # 결과값 반영
    result += count[value]

# 출력부
print(result)