# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 상수 설정
INF = 25000000

# 벨만-포드 알고리즘
def BellmanFord():
    result = [INF for _ in range(N+1)]

    # (노드의 개수 - 1)만큼 반복, 최단 경로로 가는데 노드개수만큼 이동했다는게 말안됨.
    for i in range(N-1):
        # 모든 간선에 대해 확인
        for node in range(1,N+1):
            for node_, dist in graph[node]:
                result[node_] = min(result[node_], result[node] + dist)

    # 한번 더 했을 때 갱신이 된다면, 음의 순환이 있는 것임 -> True
    for node in range(1,N+1):
        for node_, dist in graph[node]:
            if result[node_] != min(result[node_], result[node] + dist): return True
    
    # 통과했다면, return False
    return False
                    

# TC
TC = int(input())
for test_case in range(TC):
    # 입력부
    N, M, W = map(int, input().split())

    # 그래프 입력 받기
    graph = [list() for _ in range(N+1)]
    for _ in range(M): # 도로
        S, E, T = map(int, input().split())
        graph[S].append((E,T))
        graph[E].append((S,T))
    for _ in range(W): # 웜홀
        S, E, T = map(int, input().split())
        graph[S].append((E,-T))

    # 출력부
    print("YES" if BellmanFord() else "NO")