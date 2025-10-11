# 입력부
numbers = [int(input()) for _ in range(5)]

# 대표값 구하기
average = sum(numbers) // 5
numbers.sort()
center = numbers[2]

# 출력부
print(average)
print(center)