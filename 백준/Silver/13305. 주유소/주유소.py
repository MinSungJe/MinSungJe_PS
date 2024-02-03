# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# 입력부
N = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

# 누적합 구하기
dist = [0 for _ in range(N)]
for i in range(1, N): dist[i] = dist[i-1] + road[i-1]

# 초기값 선언
INF = (10**18) + 1
result = 0
DP = [0 for _ in range(N)]

# DFS(+DP)
def DFS(pos):
    if pos == N-1: return 0
    if DP[pos]: return DP[pos] # 메모이제이션
    
    # 탐색
    result = INF
    for i in range(pos+1, N):
        cost = (dist[i]-dist[pos]) * oil[pos]
        result = min(result, cost+DFS(i))
    DP[pos] = result # 메모이제이션
    return result

# 출력부
result = DFS(0)
print(result)