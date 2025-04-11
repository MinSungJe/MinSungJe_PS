# 입력부
N = int(input())
sequence = input()

# RGB index로 변환하는 함수
def getRGBIndex(letter):
    if letter == 'R': return 0
    if letter == 'G': return 1
    if letter == 'B': return 2

# 초기값 선언
idx = 0
RGB = [0, 0, 0]

# 탐색 시작
result = ''
while N:
    value =  sequence[idx]
    
    # 아직 탐색하지 않은 문자일때 확인
    if RGB[getRGBIndex(value)] == 0:
        if sum(RGB) == 2:
            RGB = [0, 0, 0]
            result += value
            N -= 1
        else: RGB[getRGBIndex(value)] = 1
    
    idx += 1

# 출력부
print(result)