# 입력부
n, k = map(int, input().split())

# 초기값 선언
pascal = [[0 for _ in range(31)] for _ in range(31)]
for i in range(31):
    pascal[i][1] = 1
    pascal[i][i] = 1

# Bottom-Up DP
for i in range(2, 30):
    for j in range(2, 30): pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

# 출력부
answer = pascal[n][k]
print(answer)