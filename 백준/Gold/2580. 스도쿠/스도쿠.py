# 입력부
Map = [list(map(int, input().split())) for _ in range(9)]

# 초기값 설정
result = False

# 배열 설정
row = [[False for _ in range(10)] for _ in range(9)]
column = [[False for _ in range(10)] for _ in range(9)]
block = [[False for _ in range(10)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        row[i][Map[i][j]] = True
        column[j][Map[i][j]] = True
        block[((i//3)*3)+j//3][Map[i][j]] = True

# DFS
def DFS(X, Y):
    global result

    # 탐색 불가 조건
    if X == 9:
        result = True
        return
    if result: return
    if Y == 9:
        DFS(X+1, 0)
        return
    if Map[X][Y]:
        DFS(X, Y+1)
        return

    # 숫자 결정
    for i in range(1,10):
        if row[X][i] or column[Y][i] or block[((X//3)*3)+Y//3][i]: continue

        # 탐색
        Map[X][Y] = i
        row[X][i] = True
        column[Y][i] = True
        block[((X//3)*3)+Y//3][i] = True

        DFS(X, Y+1) # 다음 탐색

        if not result: # backtracking
            Map[X][Y] = 0
            row[X][i] = False
            column[Y][i] = False
            block[((X//3)*3)+Y//3][i] = False

# 함수 호출
DFS(0, 0)

# 출력부
for ans in Map: print(*ans)