# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# union-find
def find(A):
    if P[A] == A: return A
    P[A] = find(P[A])
    return P[A]

def union(A, B):
    X = find(A)
    Y = find(B)
    if X == Y: return
    P[X] = Y

# DFS
def DFS(start, node, count):
    # 탐색 종료
    if node == start: return count

    # 다음 탐색
    for node_ in graph[node]:
        return DFS(start, node_, count+1)

# TC
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    s = list(map(int, input().split()))

    # 초기값 선언
    result = n
    P = [i for i in range(n+1)]
    graph = [list() for _ in range(n+1)]

    # 사이클 찾기
    for i in range(n):
        idx = i+1
        graph[idx].append(s[i])

        if find(idx) == find(s[i]):
            for node_ in graph[idx]:
                result -= DFS(idx, node_, 1)
        union(idx, s[i])
    
    # 출력부
    print(result)