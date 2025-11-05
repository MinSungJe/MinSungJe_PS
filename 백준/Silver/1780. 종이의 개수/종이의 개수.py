# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

minusPaper = 0
zeroPaper = 0
plusPaper = 0

# 정답에 더하는 함수
def add_paper(value):
    global minusPaper, zeroPaper, plusPaper
    if value == -1: minusPaper += 1
    if value == 0: zeroPaper += 1
    if value == 1: plusPaper += 1

# 분할 정복
def divide_and_conquer(X, Y, size):
    # 분할 여부 확인
    first_value = Map[X][Y]
    shouldDivide = False
    for x in range(X, X+size):
        for y in range(Y, Y+size):
            if Map[x][y] != first_value: shouldDivide = True
    
    # 정복
    if not shouldDivide:
        add_paper(first_value)
        return


    # 분할
    for x in range(X, X+size, size//3):
        for y in range(Y, Y+size, size//3): divide_and_conquer(x, y, size//3)

# 함수 호출 및 출력부
divide_and_conquer(0, 0, N)
print(minusPaper)
print(zeroPaper)
print(plusPaper)