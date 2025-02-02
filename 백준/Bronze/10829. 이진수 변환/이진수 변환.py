# 입력부
N = int(input())

# 이진수 변환
result = ""
while N:
    value = N%2
    result = str(value) + result
    N //= 2

# 출력부
print(result)