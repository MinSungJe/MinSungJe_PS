# 입력부
MKnumber = input()

# 초기값 선언
N = len(MKnumber)

# 가장 큰 숫자 구하기
result = ''
temp = 0
idx = 0
while idx < N:
    if MKnumber[idx] == 'M':
        temp += 1
    
    if MKnumber[idx] == 'K':
        result += str((10**temp) * 5) # 결과 반영
        temp = 0
    
    idx += 1

# 남은 temp 털기
for _ in range(temp): result += '1'

# 최대값 출력
print(result)

# 가장 작은 숫자 구하기
result = ''
temp = 0
idx = 0
while idx < N:
    if MKnumber[idx] == 'M': temp += 1
    
    if MKnumber[idx] == 'K':
        # 결과 반영
        if temp: result += str(10**(temp-1))
        result += '5' 
        temp = 0

    idx += 1

# 남은 temp 털기
if temp: result += str(10**(temp-1))

# 최솟값 출력
print(result)