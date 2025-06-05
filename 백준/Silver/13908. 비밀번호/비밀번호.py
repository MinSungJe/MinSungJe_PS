# 입력부
n, m = map(int, input().split())
if m != 0 : numbers = list(map(int, input().split()))

# 번호 전부 확인
result = 0
for i in range(10 ** n):
    numberSet = set(map(int, list(f'{i:0{n}}')))
    
    # 숫자가 있는지 확인
    canPassword = True
    if m != 0:
        for number in numbers:
            if not number in numberSet: canPassword = False
    if canPassword: result += 1

# 출력부
print(result)