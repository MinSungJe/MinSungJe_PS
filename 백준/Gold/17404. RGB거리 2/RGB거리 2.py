# 빠른 입력 및 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 설정
result = 0
DP = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(N)]

# DFS(+DP)
def DFS(node, house, start):
    if node == N: return 0 # 탐색 종료
    if DP[node][house][start]: return DP[node][house][start] # 메모이제이션

    # 탐색
    cost = 0
    if node != N-2: # 마지막 집이 아님
        if house == 0:
            cost = Map[node][house] + min(DFS(node+1, 1, start), DFS(node+1, 2, start))
        if house == 1:
            cost = Map[node][house] + min(DFS(node+1, 0, start), DFS(node+1, 2, start))
        if house == 2:
            cost = Map[node][house] + min(DFS(node+1, 0, start), DFS(node+1, 1, start))
    else: # 마지막 집임
        if house == 0:
            if start == 0: cost = Map[node][house] + min(DFS(node+1, 1, start), DFS(node+1, 2, start))
            if start == 1: cost = Map[node][house] + DFS(node+1, 2, start)
            if start == 2: cost = Map[node][house] + DFS(node+1, 1, start)
        if house == 1:
            if start == 0: cost = Map[node][house] + DFS(node+1, 2, start)
            if start == 1: cost = Map[node][house] + min(DFS(node+1, 0, start), DFS(node+1, 2, start))
            if start == 2: cost = Map[node][house] + DFS(node+1, 0, start)
        if house == 2:
            if start == 0: cost = Map[node][house] + DFS(node+1, 1, start)
            if start == 1: cost = Map[node][house] + DFS(node+1, 0, start)
            if start == 2: cost = Map[node][house] + min(DFS(node+1, 0, start), DFS(node+1, 1, start))
    
    DP[node][house][start] = cost
    return cost        

# 함수 호출 및 출력부
result = min(DFS(0,0,0), DFS(0,1,1), DFS(0,2,2))
print(result)