# 입력부
N, M = map(int, input().split())

# 초기값 선언
visited = [0 for _ in range(N+1)]

# DFS
def DFS(count, record: list, previous):
    global visited
    # 탐색 완료
    if count == M:
        print(*record)
        return

    # 다음 탐색
    for i in range(1, N+1):
        if visited[i] < M and previous <= i:
            visited[i] += 1
            DFS(count+1, record + [i], i)
            visited[i] -= 1

# 함수 출력
DFS(0, [], 0)