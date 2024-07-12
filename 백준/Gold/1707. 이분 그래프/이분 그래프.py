# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# BFS 함수 선언
def DFS(node, Type):
    # 탐색 불가 조건
    if group[node] != -1:
        if group[node] != Type: return False
        return True
    
    # 탐색
    group[node] = Type

    # 다음 탐색
    Type_ = 1 - Type
    for node_ in graph[node]:
        if not DFS(node_, Type_): return False
    
    return True

# TC
K = int(input())
for test_case in range(1, K+1):
    # 입력부
    V, E = map(int, input().split())
    graph = [list() for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 초기값 선언
    group = [-1 for _ in range(V+1)]

    # 모든 정점 탐색
    result = True
    for node in range(1, V+1):
        if group[node] != -1: continue
        if not DFS(node, 0):
            result = False
            break

    # 출력부
    print('YES' if result else 'NO')