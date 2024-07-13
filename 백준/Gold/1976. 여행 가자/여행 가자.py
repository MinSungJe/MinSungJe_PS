# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
M = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

# 초기값 선언
INF = 201

# 연결되어있지 않은 부분 INF로 채우기
for i in range(N):
    for j in range(N):
        if i != j and not Map[i][j]: Map[i][j] = INF

# 플로이드-워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            Map[i][j] = min(Map[i][j], Map[i][k]+Map[k][j])

# 여행 계획 확인
result = 'YES'
for i in range(M-1):
    city = plan[i] - 1
    city_ = plan[i+1] - 1
    if Map[city][city_] != INF: continue
    result = 'NO'
    break

# 출력부
print(result)