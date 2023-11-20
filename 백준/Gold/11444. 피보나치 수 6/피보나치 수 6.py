# 입력부
n = int(input())

# 초기값 선언
M = [[1, 1], [1, 0]]
mod = 1000000007

# 2*2 행렬 곱 구하는 함수
def matrixMultiply(A, B):
    resultMatrix = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                resultMatrix[i][j] += (A[i][k] * B[k][j]) % mod
    
    return resultMatrix

# 분할 정복을 이용한 거듭제곱
def MMultiply(n):
    # 분할 완료
    if n == 1: return M

    # 분할
    if n % 2 == 0: # n이 짝수인 경우
        temp = MMultiply(n//2)
        return matrixMultiply(temp, temp)
    
    else: # n이 홀수인 경우
        temp = MMultiply(n-1)
        return matrixMultiply(temp, M)

# 출력부
print(MMultiply(n-1)[0][0] % mod if n != 1 else 1)