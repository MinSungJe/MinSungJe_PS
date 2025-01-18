# 입력부
k = int(input())

# 초기값 선언
grass = [[1 for _ in range(10)] for _ in range(10)]

# 자라는 함수
def grow():
    for i in range(10):
        for j in range(10): grass[i][j] += 1

# row로 자르기 함수
def cutRow(number):
    for i in range(10): grass[number-1][i] = 1

# column으로 자르기 함수
def cutColumn(number):
    for i in range(10): grass[i][number-1] = 1

# 잔디 자르기
for _ in range(k):
    row1, row2, row3, col1, col2, col3 = map(int, input().split())
    grow()
    for row in (row1, row2, row3): cutRow(row)
    for col in (col1, col2, col3): cutColumn(col)

# 출력부
for i in range(10): print(*grass[i])