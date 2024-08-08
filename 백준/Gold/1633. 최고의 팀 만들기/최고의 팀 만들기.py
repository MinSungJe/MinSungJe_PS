# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
team = list()
while True:
    try:
        # 입력부
        W, B = map(int, input().split())
        team.append((W, B))
    except: break

# 초기값 선언
N = len(team)
DP = [[[0 for _ in range(N)] for _ in range(16)] for _ in range(16)]
INF = 100001

# DFS(+DP)
def DFS(W, B, idx):
    # 탐색 종료
    if W == 15 and B == 15: return 0
    if idx == N: return -INF

    # 메모이제이션
    if DP[W][B][idx]: return DP[W][B][idx]

    # 다음 탐색
    result = 0
    
    # 이 선수를 W로 선정
    if W < 15:
        value = team[idx][0] + DFS(W+1, B, idx+1)
        result = max(result, value)

    # 이 선수를 B로 선정
    if B < 15:
        value = team[idx][1] + DFS(W, B+1, idx+1)
        result = max(result, value)

    # 이 선수를 아무것도 선정하지 않음
    value = DFS(W, B, idx+1)
    result = max(result, value)

    # 메모
    DP[W][B][idx] = result
    return result

# 함수 호출 및 출력부
result = DFS(0, 0, 0)
print(result)