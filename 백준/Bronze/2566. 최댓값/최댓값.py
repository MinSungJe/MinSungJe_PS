# 입력부
numbers = [list(map(int, input().split())) for _ in range(9)]

# 최댓값 구하기
result = -1
X, Y = 1, 1
for x in range(9):
    for y in range(9):
        value = numbers[x][y]
        if value > result:
            X, Y = x+1, y+1
            result = value

# 출력부
print(result)
print(X, Y)