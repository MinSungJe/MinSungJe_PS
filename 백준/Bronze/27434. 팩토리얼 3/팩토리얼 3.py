# 입력부
N = int(input())

# 팩토리얼 구하기
result = 1
for number in range(1, N+1):
    result *= number

# 출력부
print(result)