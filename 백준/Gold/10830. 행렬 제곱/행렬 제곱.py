# 입력부
N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
normalMatrix = [[1 if i == j else 0 for i in range(N)] for j in range(N)]

# 행렬제곱
def matmul(A, B):
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                temp[i][j] += A[i][k] * B[k][j]
                temp[i][j] = temp[i][j] % 1000
    return temp

# 분할정복을 이용한 거듭제곱
def multiply(M, N):
    # 분할 완료
    if N == 1: return matmul(matrix, normalMatrix)

    # 분할
    if N % 2 == 0:
        segmat = multiply(M, N//2)
        return matmul(segmat, segmat)
    
    else:
        segmat = multiply(M, N-1)
        return matmul(segmat, matrix)

# 출력부
result = multiply(matrix,B)
for row in result:
    print(*row)