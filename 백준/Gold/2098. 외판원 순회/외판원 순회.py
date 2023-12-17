# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 설정
INF = 16000001
DP = [[0 for _ in range(1<<N)] for _ in range(N)]

# DFS(+DP)
def DFS(node, visited):
    # 전체 순회 완료
    if visited == (1<<N)-1:
        if Map[node][0]: return Map[node][0]
        else: return INF
    
    # 메모이제이션
    if DP[node][visited]: return DP[node][visited]

    # 다음 탐색
    min_dist = INF
    for node_ in range(1, N):
        # 탐색 불가 조건
        if not Map[node][node_]: continue
        if visited & 1<<node_: continue

        # 탐색
        dist = Map[node][node_] + DFS(node_, visited|1<<node_)
        min_dist = min(dist, min_dist)
    
    DP[node][visited] = min_dist
    return DP[node][visited]
    

# 함수 호출 및 출력부
result = DFS(0,1)
print(result)