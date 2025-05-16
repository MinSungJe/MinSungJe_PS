# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())

# 초기값 선언
queue = deque()

# 명령
for _ in range(N):
    cmd = input().split()

    # 출력부
    match cmd[0]:
        case "1": queue.appendleft(cmd[1])
        case "2": queue.append(cmd[1])
        case "3": print(queue.popleft() if queue else -1)
        case "4": print(queue.pop() if queue else -1)
        case "5": print(len(queue))
        case "6": print(1 if not queue else 0)
        case "7": print(queue[0] if queue else -1)
        case "8": print(queue[-1] if queue else -1)
        case default: continue