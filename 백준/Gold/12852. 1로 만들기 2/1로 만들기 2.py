# 입력부
X = int(input())

# DP 배열 및 기록 배열 선언
DP = [0 for _ in range(X+1)]
previous = [0 for _ in range(X+1)]
INF = 1000001
DP[0] = INF
DP[1] = 0

# DP 배열 채우기
for i in range(2, X+1):
    min_value, min_index = DP[i-1]+1 ,i-1
    if i % 2 == 0:
        value = DP[i//2] + 1
        if min_value > value: min_value, min_index = value, i//2
    if i % 3 == 0:
        value = DP[i//3] + 1
        if min_value > value: min_value, min_index = value, i//3
    
    DP[i] = min_value
    previous[i] = min_index

# 출력부
answer = DP[X]
tracking = []
index = X
while index > 0:
    tracking.append(index)
    index = previous[index]
print(answer)
print(*tracking)