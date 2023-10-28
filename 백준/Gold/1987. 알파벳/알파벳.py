# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
R, C = map(int, input().split())
Map = [list(input()) for _ in range(R)]

# 초기값 설정
visited = [[False for _ in range(C)] for _ in range(R)]
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
result = 0

# DFS(재귀)
def DFS(X, Y, count, record):
    global result

    # result 갱신
    if count > result: result = count

    # 다음 탐색
    for i in range(4):
        X_ = X + dx[i]
        Y_ = Y + dy[i]
        
        # 탐색 불가 조건
        # 1. 탐색하려는 구역은 범위를 벗어남
        if X_ < 0 or X_ >= R or Y_ < 0 or Y_ >= C: continue
        # 2. 탐색하려는 구역은 알파벳 중복 지역임
        if Map[X_][Y_] in record: continue
        # 3. 탐색하려는 구역은 이미 방문한 곳임
        if visited[X_][Y_]: continue

        # 탐색
        visited[X_][Y_] = True
        record.add(Map[X_][Y_])

        DFS(X_, Y_, count+1, record)

        # backtracking
        visited[X_][Y_] = False
        record.remove(Map[X_][Y_])

# 실행 및 출력부
DFS(0,0,1,set(Map[0][0]))
print(result)