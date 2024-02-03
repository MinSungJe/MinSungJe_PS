# 입력부
N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 누적합 구하기
dist = [0 for _ in range(N)]
for i in range(1,N): dist[i] = dist[i-1] + road[i-1]

# 초기값 선언
result = 0
last_pos = 0
min_cost = cost[last_pos]

for pos in range(1, N):
    if min_cost >= cost[pos]: # 값이 비싸지지 않은 경우 지불(그리디)
        result += (dist[pos]-dist[last_pos]) * min_cost
        min_cost = cost[pos]
        last_pos = pos

# 계산이 되지 않은 부분 더해주기
result += (dist[N-1]-dist[last_pos]) * min_cost

# 출력부
print(result)