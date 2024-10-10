# 입력부
N = int(input())

# 초기값 선언
visited = [False for _ in range(N+1)]

# DFS 선언
def DFS(idx, L):
    if idx == N:
        print(*L) # 출력부
        return
    
    # 숫자 추가
    for number in range(1, N+1):
        # 탐색 불가 조건
        if visited[number]: continue

        # 탐색
        visited[number] = True
        DFS(idx+1, L+[number])

        # backtracking
        visited[number] = False

# 함수 호출
DFS(0, [])