# 입력부
M, N = map(int, input().split())

# 숫자를 문자로 변환
def changeIntToString(number):
    result = ''
    for digit in str(number):
        if digit == '0': result += 'zero'
        if digit == '1': result += 'one'
        if digit == '2': result += 'two'
        if digit == '3': result += 'three'
        if digit == '4': result += 'four'
        if digit == '5': result += 'five'
        if digit == '6': result += 'six'
        if digit == '7': result += 'seven'
        if digit == '8': result += 'eight'
        if digit == '9': result += 'nine'
    return result

# 숫자 dictionary 넣기
numberDict = dict()
for number in range(M, N+1):
    numberDict[changeIntToString(number)] = number

# 정렬된 키 배열 구하기
numberIdx = sorted(numberDict.keys())

# 출력부
for i in range(len(numberIdx)):
    print(numberDict[numberIdx[i]], end=' ')
    if i % 10 == 9: print('\n', end='')