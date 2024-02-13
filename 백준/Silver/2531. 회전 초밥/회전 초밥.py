# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, d, k, c = map(int, input().split())
lane = list()
for _ in range(N):
    lane.append(int(input()))

# 모든 경우 확인
result = 0
for i in range(N):
    line = [c]
    for j in range(k):
        idx = 0
        if i+j >= N: idx = i+j-N
        else: idx = i+j
        line.append(lane[idx])
    
    result = max(result, len(set(line)))

# 출력부
print(result)