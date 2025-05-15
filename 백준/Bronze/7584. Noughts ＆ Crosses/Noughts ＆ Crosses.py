# 빙고 확인
def check_tictactoe(Map):
    row = Map + [0 * (9-len(Map))]

    result = [False, False]
    if row[0] == 0 and row[1] == 0 and row[2] == 0: result[0] = True
    if row[3] == 0 and row[4] == 0 and row[5] == 0: result[0] = True
    if row[6] == 0 and row[7] == 0 and row[8] == 0: result[0] = True
    if row[0] == 0 and row[3] == 0 and row[6] == 0: result[0] = True
    if row[1] == 0 and row[4] == 0 and row[7] == 0: result[0] = True
    if row[2] == 0 and row[5] == 0 and row[8] == 0: result[0] = True
    if row[0] == 0 and row[4] == 0 and row[8] == 0: result[0] = True
    if row[2] == 0 and row[4] == 0 and row[6] == 0: result[0] = True

    if row[0] == 1 and row[1] == 1 and row[2] == 1: result[1] = True
    if row[3] == 1 and row[4] == 1 and row[5] == 1: result[1] = True
    if row[6] == 1 and row[7] == 1 and row[8] == 1: result[1] = True
    if row[0] == 1 and row[3] == 1 and row[6] == 1: result[1] = True
    if row[1] == 1 and row[4] == 1 and row[7] == 1: result[1] = True
    if row[2] == 1 and row[5] == 1 and row[8] == 1: result[1] = True
    if row[0] == 1 and row[4] == 1 and row[8] == 1: result[1] = True
    if row[2] == 1 and row[4] == 1 and row[6] == 1: result[1] = True

    if result[0] and result[1]: return 'Draw'
    if result[0]: return 'O'
    if result[1]: return 'X'
    return 'Draw'


# 입력부
while True:
    cmd = input().split()
    
    # 종료
    if cmd[0] == '#': break

    # 체크하기
    numbers = list(map(int, cmd[1:]))
    Map = [-1 for _ in range(9)]
    turn = 0 if cmd[0] == 'O' else 1
    for number in numbers:
        Map[number-1] = turn
        turn = 1-turn
    
    # 출력부
    print(check_tictactoe(Map))