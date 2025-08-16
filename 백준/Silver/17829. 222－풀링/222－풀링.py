# 입력부
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

# K 얻어내기
K = 0
for i in range(1, 11):
    if 2 ** i == N: K = i


# 분할정복
def divideConquer(x_start, y_start, value):
    # 분할
    if value != 2:
        divideConquer(x_start, y_start, value // 2)
        divideConquer(x_start+value//2, y_start, value // 2)
        divideConquer(x_start, y_start+value//2, value // 2)
        divideConquer(x_start+value//2, y_start+value//2, value // 2)
        return
    
    # 두 번째로 큰 수 확인
    numbers = [Map[x_start][y_start], Map[x_start][y_start+1], Map[x_start+1][y_start], Map[x_start+1][y_start+1]]
    numbers.sort()
    second_number = numbers[2]
    Map[x_start//2][y_start//2] = second_number

# K번 반복
for k in range(K):
    divideConquer(0, 0, N // (2 ** k))

# 출력부
answer = Map[0][0]
print(answer)