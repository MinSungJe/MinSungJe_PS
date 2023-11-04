# 입력부
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 초기값 선언
visited = [False for _ in range(N)]
result = []
numbers.sort()

# DFS 선언
def DFS(idx):
    global result

    # 출력부
    if idx == M:
        print(*result)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(numbers[i])
            DFS(idx+1)
            visited[i] = False
            result.remove(numbers[i])
            
# DFS 실행
DFS(0)