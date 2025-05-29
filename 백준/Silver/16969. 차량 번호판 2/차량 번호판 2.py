# 입력부
board = input()

# 초기값 선언
result = 10 if board[0] == 'd' else 26
BIG_NUMBER = 1000000009

# 조합
for i in range(1, len(board)):
    target = board[i]
    if target == 'd':
        if board[i-1] == 'd': result = (result * 9) % BIG_NUMBER
        if board[i-1] == 'c': result = (result * 10) % BIG_NUMBER
    if target == 'c':
        if board[i-1] == 'd': result = (result * 26) % BIG_NUMBER
        if board[i-1] == 'c': result = (result * 25) % BIG_NUMBER

# 출력부
print(result)