# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, P = map(int, input().split())

# 초기값 선언
finger = [list() for _ in range(7)]

# 플랫 짚기
result = 0
for _ in range(N):
    line, flat = map(int, input().split())
    flat *= -1
    
    while finger[line] and finger[line][0] < flat:
        heapq.heappop(finger[line])
        result += 1
    
    if finger[line] and finger[line][0] == flat: continue
    heapq.heappush(finger[line], flat)
    result += 1

# 출력부
print(result)