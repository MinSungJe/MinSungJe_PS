# 입력부
N = int(input())

# N을 2진수 변환
binN = f"{N:b}"

# 결과값 구하기
result = 0
for i in range(len(binN)):
    value = 3 ** (len(binN)-i-1)
    if binN[i] == '1': result += value

# 출력부
print(result)