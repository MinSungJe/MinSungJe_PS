# 빠른 입력 / 재귀 제한 해제
import sys
def input(): return sys.stdin.readline()
sys.setrecursionlimit(10**6)

# 입력부 및 초기값 선언
N, M = map(int, input().split())
edge = [list() for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    edge[A].append(B)
    edge[B].append(A)
result = 0

# DFS(재귀)
def DFS(pos):
    global visited
    # 탐색 불가 조건 : 이미 방문한 적 있음
    if visited[pos]: return

    # 탐색
    visited[pos] = True

    # 다음 탐색
    for next in edge[pos]:
        DFS(next)

# 결과값 계산 및 출력
for i in range(1,N+1):
    if not visited[i]:
        DFS(i)
        result += 1

print(result)