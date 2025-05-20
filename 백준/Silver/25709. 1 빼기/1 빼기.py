# 입력부
N = int(input())

# 1을 제거하는 함수
def remove_one(number):
    result = 0
    letter = ''
    for digit in str(number):
        if digit == '1':
            result += 1
            continue
        letter += digit
    
    return (result, int(letter) if letter else 0)

# 1 빼기 실행
result = 0
while N:
    value, N = remove_one(str(N))
    
    if value:
        result += value
        continue

    N -= 1
    result += 1

# 출력부
print(result)