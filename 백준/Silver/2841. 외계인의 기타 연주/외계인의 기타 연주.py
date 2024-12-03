# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, P = map(int, input().split())

# 초기값 선언
finger = [deque() for _ in range(7)]

# 플랫 짚기
result = 0
for _ in range(N):
    line, flat = map(int, input().split())
    
    while finger[line] and finger[line][0] > flat:
        finger[line].popleft()
        result += 1
    
    if finger[line] and finger[line][0] == flat: continue
    finger[line].appendleft(flat)
    result += 1

# 출력부
print(result)