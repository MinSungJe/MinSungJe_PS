# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())
m = int(input())
graph = [list() for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 초기값 선언
visited = [501 for _ in range(n+1)]

# DFS
def DFS(idx, count):
    # 탐색 종료
    if visited[idx] <= count: return

    # 탐색
    visited[idx] = count

    # 다음 탐색
    for idx_ in graph[idx]: DFS(idx_, count+1)

# 함수 호출
DFS(1, 0)

# 결과 도출 및 출력부
answer = 0
for i in range(2, n+1):
    if visited[i] <= 2: answer += 1
print(answer)