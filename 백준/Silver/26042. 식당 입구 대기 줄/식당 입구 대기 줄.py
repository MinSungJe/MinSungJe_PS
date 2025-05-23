# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())

# 초기값 선언
line = deque()
max_length = 0
index = 0

for _ in range(n):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        line.append(cmd[1])

        # 줄 비교
        line_length = len(line)
        if max_length < line_length:
            max_length = line_length
            index = cmd[1]
        if max_length == line_length:
            index = min(cmd[1], index)
    
    if cmd[0] == 2: line.popleft()

# 출력부
print(max_length, index)