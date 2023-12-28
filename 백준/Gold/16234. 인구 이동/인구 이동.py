# 빠른 입력 및 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, L, R = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# DFS
def DFS(X, Y):
    visited[X][Y] = True
    result = [[X, Y, Map[X][Y]]]

    # 다음 탐색
    for i in range(4):
        X_, Y_ = X + dx[i], Y + dy[i]
        # 탐색 불가 조건
        if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N: continue
        if visited[X_][Y_]: continue
        limit = abs(Map[X][Y]-Map[X_][Y_])
        if limit < L or limit > R: continue

        # 탐색
        visited[X_][Y_] = True

        # 결과 추가
        result += DFS(X_, Y_)

    return result

# 함수 호출
result = 0
while True:
    group = list()
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]: group.append(DFS(i,j))

    # 경계가 하나도 안열린 경우 종료
    if len(group) == N*N: break

    # 열린 경계 간 인구 이동
    for g in group:
        Sum = 0
        Count = len(g)
        for region in g:
            Sum += region[2]
        Avg = Sum // Count
        for region in g:
            X, Y = region[0], region[1]
            Map[X][Y] = Avg

    result += 1

# 출력부
print(result)