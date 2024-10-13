# 입력부
N, M = map(int, input().split())
Map = [list(map(int, list(input()))) for _ in range(N)]

# 초기값 선언
L = N * M
INF = 40000
DP = [[-1 for _ in range(1<<L)] for _ in range(L)]

# idx 찾아주는 함수
def findIndex(X, Y): return M*X + Y

# DFS
def DFS(X, Y, visited):
    idx = findIndex(X, Y)

    # 탐색 종료
    if idx >= L: return 0
    if visited & (1 << idx):
        if Y+1 == M: return DFS(X+1, 0, visited)
        return DFS(X, Y+1, visited)

    # 메모이제이션
    if DP[idx][visited] != -1: return DP[idx][visited]

    # 다음 탐색
    result = Map[X][Y]

    # 가로 탐색
    value = 0
    visited_ = visited
    for i in range(M):
        Y_ = Y+i
        checked_visited = 1 << findIndex(X, Y_)

        # 탐색 불가 조건
        if visited & checked_visited: break

        # 탐색
        visited_ = visited_ | checked_visited
        value = (value * 10) + Map[X][Y_]

        # 끝까지 도착했는지 여부에 따라 다음 탐색 위치 달라짐
        if Y_ == M-1:
            result = max(result, value+DFS(X+1, 0, visited_))
            break
        result = max(result, value+DFS(X, Y+1, visited_))
    
    # 세로 탐색
    value = 0
    visited_ = visited
    for i in range(N):
        X_ = X+i
        checked_visited = 1 << findIndex(X_, Y)

        # 탐색
        visited_ = visited_ | checked_visited
        value = (value * 10) + Map[X_][Y]

        # 끝까지 도착했는지 여부에 따라 다음 탐색 위치 달라짐
        if Y+1 == M: result = max(result, value+DFS(X+1, 0, visited_))
        else: result = max(result, value+DFS(X, Y+1, visited_))
        if X_ == N-1: break
    
    # 메모이제이션
    DP[idx][visited] = result
    return result

# 함수 호출 및 출력부
result = DFS(0, 0, 0)
print(result)