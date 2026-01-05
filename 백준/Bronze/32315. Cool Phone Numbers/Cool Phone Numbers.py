# 입력부
number = input()

# 숫자 기록
digits = set()
for digit in number:
    if digit == '-': continue
    digits.add(digit)

# 출력부
answer = len(digits)
print(answer)