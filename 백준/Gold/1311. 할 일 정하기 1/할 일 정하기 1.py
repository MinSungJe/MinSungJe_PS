# 입력부
N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
visited = 0
DP = [[0 for _ in range((1<<N)-1)] for _ in range(N)]
INF = 200001

# DFS(+DP)
def DFS(idx, visited):
    # 탐색 종료
    if idx == N: return 0
    if DP[idx][visited]: return DP[idx][visited] # 메모이제이션

    # 다음 탐색
    result = INF
    for i in range(N):
        # 탐색 불가 조건
        if visited & (1 << i): continue
        result = min(result, D[idx][i]+DFS(idx+1, (visited|1<<i)))

    DP[idx][visited] = result
    return result

# 함수 호출 및 출력부
result = DFS(0, 0)
print(result)