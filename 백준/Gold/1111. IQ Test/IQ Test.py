# 모듈 불러오기
from collections import deque

# 입력부
N = int(input())
numbers = list(map(int, input().split()))

# 처음 수열을 이어나갈 수 있는 경우 모두 넣기
queue = deque()
for a in range(-200, 201):
    if N != 1: b = numbers[1] - a*numbers[0]
    else: b = 0
    queue.append((a, b))

# 수열을 이어나갈 수 있는지 여부 확인
for i in range(1, N-1):
    temp = deque()
    while queue:
        a, b = queue.popleft()
        if a*numbers[i] + b == numbers[i+1]: temp.append((a, b))
    while temp: queue.append(temp.popleft())

# 모든 경우 계산
result = set()
while queue:
    a, b = queue.popleft()
    result.add(a*numbers[N-1]+b)

# 출력부
if len(result) == 0: print('B')
elif len(result) > 1 or N == 1: print('A')
else: print(*result)