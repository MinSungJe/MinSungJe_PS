# 입력부
A, B = map(int, input().split())

# 시그마 함수
def sigmaFromOne(number):
    return (number+1) * number // 2

# 계산
if A > B: result = sigmaFromOne(A) - sigmaFromOne(B-1)
else: result = sigmaFromOne(B) - sigmaFromOne(A-1)

# 출력부
print(result)