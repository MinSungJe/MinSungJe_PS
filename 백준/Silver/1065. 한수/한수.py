# 입력부
N = int(input())

# 한수인지 아닌지 확인하는 함수
def checkIsHansu(number):
    digits = list(map(int, list(str(number))))

    # 숫자가 하나 있으면, 한수임`
    if len(digits) == 1: return True

    # 한수 체크
    result = True
    gap = digits[1] - digits[0]
    for i in range(1, len(digits)):
        if digits[i] - digits[i-1] != gap: result = False
    
    return result

# 함수 호출
result = 0
for number in range(1, N+1):
    if checkIsHansu(number): result += 1

# 출력부
print(result)