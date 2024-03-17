# 입력부
N, M = map(int, input().split())

# DFS
def DFS(numbers):
    if len(numbers) == M:
        print(*numbers)
        return
    
    for i in range(1, N+1): DFS(numbers+[i])

# 함수 호출
DFS(list())