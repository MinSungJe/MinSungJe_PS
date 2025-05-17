# 초기값 선언
result = [True for _ in range(10100)]

# 셀프 넘버가 아닌 숫자 기록
for number in range(1, 10001):
    idx = number
    for digit in str(number): idx += int(digit)
    result[idx] = False

# 출력부
for self_number in range(1, 10001):
    if result[self_number]: print(self_number)