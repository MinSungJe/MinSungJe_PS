# 입력부
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

# 초기값 선언
visited = [False for _ in range(N)]

# DFS
def DFS(count, record, previous):
    # 탐색 완료
    if count == M:
        print(*record)
        return
    
    # 다음 탐색
    for i in range(N):
        if visited[i] < M and previous <= numbers[i]:
            visited[i] += 1
            DFS(count+1, record+[numbers[i]], numbers[i])
            visited[i] -= 1

# 함수 호출
DFS(0, [], 0)