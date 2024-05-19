# 입력부
N = int(input())

# 5로 나눈 나머지에 따라 결과값이 달라짐
if N % 5 == 0 or N % 5 == 2: result = 'CY'
else: result = 'SK'

# 출력부
print(result)