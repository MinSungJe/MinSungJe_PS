# 입력부
n = int(input())
A = list(map(int, input().split()))
s = int(input())

# 초기값 선언
visited = [0 for _ in range(n)]

# DFS
def DFS(node):
    # 탐색 불가 조건
    if node < 0 or node >= n: return
    if visited[node] == 1: return

    # 탐색
    visited[node] = 1

    # 다음 탐색
    value = A[node]
    for node_ in (node+value, node-value): DFS(node_)

# 함수 호출 및 출력부
DFS(s-1)
print(sum(visited))