# 조합 계산
def getCombination(n, m):
    if n < m: return 0
    return int(getFactorial(n) / (getFactorial(n-m) * getFactorial(m)))

# 팩토리얼 계산
def getFactorial(n):
    result = 1
    for i in range(1, n+1): result *= i
    return result

# 입력부
J = int(input())

# 출력부
print(getCombination(J-1, 3))