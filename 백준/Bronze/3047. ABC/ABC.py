# 입력부
numbers = list(map(int, input().split()))
letters = list(input())

# 숫자 정렬
numbers.sort()

# 결과 도출
answer = list()
for letter in letters:
    if letter == 'A': answer.append(numbers[0])
    if letter == 'B': answer.append(numbers[1])
    if letter == 'C': answer.append(numbers[2])

# 출력부
print(*answer)