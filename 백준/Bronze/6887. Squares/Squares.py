# 압력부
square = int(input())

# 값 구하기
result = 0
for i in range(1, 10001):
    if i * i > square: break
    result = i

# 출력부
print(f"The largest square has side length {result}.")