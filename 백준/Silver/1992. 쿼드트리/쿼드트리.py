# 입력부
N = int(input())
Map = [list(map(int, list(input()))) for _ in range(N)]

# 분할 정복
def divide_and_conquer(x, y, size):
    first_value = str(Map[x][y])
    if size == 1: return first_value

    result = ''

    require_divide = False

    for x_ in range(x, x+size):
        for y_ in range(y, y+size):
            value = str(Map[x_][y_])
            if value != first_value: require_divide = True

    if not require_divide: result += first_value
    else:
        result += '('
        for X, Y in ((x, y), (x, y+size//2), (x+size//2, y), (x+size//2, y+size//2)):
            result += divide_and_conquer(X, Y, size//2)
        result += ')'
    
    return result

# 출력부
answer = divide_and_conquer(0, 0, N)
print(answer)