# 전역변수 선언
dx = (0, -1, 1, 0, 0)
dy = (0, 0, 0, -1, 1)

# *과 .을 변환하는 함수
def change_mark(mark):
    if mark == '*': return 1
    if mark == '.': return 0
    return -1

# 입력부
P = int(input())
for _ in range(P):
    board = [list(map(change_mark, list(input()))) for _ in range(3)]
    
    # 초기값 선언
    answer = [10]

    # DFS
    def DFS(x, y, count):
        # 보드 확인
        is_white = True
        for X in range(3):
            for Y in range(3):
                if board[X][Y]: is_white = False
        if is_white: answer[0] = min(answer[0], count)

        # 탐색 종료
        if x >= 3: return

        # 뒤집기
        for i in range(5):
            x_, y_ = x+dx[i], y+dy[i]
            if x_ < 0 or x_ >= 3 or y_ < 0 or y_ >= 3: continue
            board[x_][y_] = 1-board[x_][y_]

        # 다음 대상 탐색
        if y+1 >= 3: DFS(x+1, 0, count+1)
        else: DFS(x, y+1, count+1)

        # 백트래킹
        for i in range(5):
            x_, y_ = x+dx[i], y+dy[i]
            if x_ < 0 or x_ >= 3 or y_ < 0 or y_ >= 3: continue
            board[x_][y_] = 1-board[x_][y_]

        # 다음 대상 탐색
        if y+1 >= 3: DFS(x+1, 0, count)
        else: DFS(x, y+1, count)

    # 함수 호출
    DFS(0, 0, 0)
    
    # 출력부
    print(answer[0])