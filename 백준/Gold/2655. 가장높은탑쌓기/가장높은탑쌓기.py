# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
bricks = [[i+1]+list(map(int, input().split())) for i in range(N)]

# 무게 순으로 정렬
bricks.sort(key=lambda x:-x[3])

# DP 배열 선언
DP = [0 for _ in range(N)]


# DP 배열 채우기
for i in range(N):
    DP[i] = bricks[i][2]
    for j in range(i):
        if bricks[i][1] < bricks[j][1]: DP[i] = max(DP[i], bricks[i][2]+DP[j])

# 역추적
result = list()
value = max(DP)
idx = N-1
while idx >= 0:
    if DP[idx] == value:
        result.append(bricks[idx][0])
        value -= bricks[idx][2]
    idx -= 1

# 출력부
print(len(result))
for i in range(len(result)): print(result[i])