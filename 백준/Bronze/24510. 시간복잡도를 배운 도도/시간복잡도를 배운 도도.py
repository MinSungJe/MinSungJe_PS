# 입력부
C = int(input())

# 모든 코드에서 찾기
result = 0
for _ in range(C):
    code = input()
    value = 0

    for i in range(len(code)):
        letter = code[i]

        # f, w인 경우 확인
        if letter == 'f' and i+2 < len(code):
            if code[i+1] == 'o' and code[i+2] == 'r': value += 1 # for 확인
        if letter == 'w' and i+4 < len(code):
            if code[i+1] == 'h' and code[i+2] == 'i' and code[i+3] == 'l' and code[i+4] == 'e': value += 1 # while 확인
        
    # 결과값 반영
    result = max(result, value)

# 출력부
print(result)