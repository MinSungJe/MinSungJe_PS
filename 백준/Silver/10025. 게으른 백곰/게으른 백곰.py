# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 초기값 선언
MAX = 1000001

# 입력부
N, K = map(int, input().split())
zoo = [0 for _ in range(MAX+1)]
for _ in range(N):
    g, x = map(int, input().split())
    zoo[x] = g

# 슬라이딩 윈도우
l = 0
r = 2*K + 1
temp = sum(zoo[l:min(MAX, r)])
answer = temp
while r < MAX:
    temp -= zoo[l]
    temp += zoo[r]
    l += 1
    r += 1
    answer = max(answer, temp)

# 출력부
print(answer)