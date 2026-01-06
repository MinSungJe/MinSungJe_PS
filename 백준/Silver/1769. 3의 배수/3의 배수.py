# 입력부
X = int(input())

# 자릿수 더하기
def sum_digits(number):
    result = 0
    for digit in str(number): result += int(digit)
    return result

# 한 자릿수가 되기까지 더하기
answer = 0
while X > 9:
    answer += 1
    X = sum_digits(X)

# 출력부
print(answer)
print('YES' if X in [3, 6, 9] else 'NO')