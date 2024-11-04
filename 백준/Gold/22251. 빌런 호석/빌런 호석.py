# 입력부
N, K, P, X = map(int, input().split())

# 숫자 정보 입력
numbers = [[1,1,1,0,1,1,1], [0,0,1,0,0,1,0], [1,0,1,1,1,0,1], [1,0,1,1,0,1,1], [0,1,1,1,0,1,0], [1,1,0,1,0,1,1], [1,1,0,1,1,1,1], [1,0,1,0,0,1,0], [1,1,1,1,1,1,1], [1,1,1,1,0,1,1]]
graph = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        for pos in range(7):
            if numbers[i][pos] != numbers[j][pos]: graph[i][j] += 1

# 숫자 앞에 0붙이는 함수
def putZero(number):
    return f"{number:0{K}d}"

# 모든 숫자에 대해 탐색
result = 0
X_ = putZero(X)
for number in range(1, N+1):
    number_ = putZero(number)
    changed_count = 0
    for pos in range(K): changed_count += graph[int(X_[pos])][int(number_[pos])]
    if 1 <= changed_count <= P: result += 1

# 출력부
print(result)