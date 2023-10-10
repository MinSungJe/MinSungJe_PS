# 입력부
equation = input()

# 초기값 선언
temp = ''
result = 0
minus = False

# 계산 시작
for i in range(len(equation)):
    if equation[i] == '+': # + 기호를 만났을 때
        if minus: # -가 앞에 있었다면
            result -= int(temp) # 값을 빼준다.
        else: # -가 앞에 없었다면
            result += int(temp) # 값을 더해준다.

        # temp 초기화 
        temp = ''

    elif equation[i] == '-': # - 기호를 만났을때
        if minus: # -가 앞에 있었다면
            result -= int(temp) # 값을 빼준다.
        else: # -가 앞에 없었다면
            result += int(temp) # 값을 더해준다.
            minus = True # -가 있었다고 기록, 앞으로 어떤 기호가 나오던 전부 값을 빼준다.
        
        # temp 초기화
        temp = ''

    else: # 숫자라면 temp에 문자를 넣는다
        temp += equation[i]

# 수식이 끝났으니 마무리
if minus: result -= int(temp) # -가 식에 있었다면 값을 빼준다.
else: result += int(temp) # -가 식에 없었다면 값을 더한다.

# 출력부
print(result)