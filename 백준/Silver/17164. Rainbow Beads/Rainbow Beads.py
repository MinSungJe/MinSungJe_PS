# 입력부
N = int(input())
jewel_original = input()

# 두 색맹에게 보이는 보석 배치 만들기
jewel_red, jewel_blue = '', ''
for jewel in jewel_original:
    if jewel == 'V':
        jewel_red += 'R'
        jewel_blue += 'B'
    else:
        jewel_red += jewel
        jewel_blue += jewel

# 반복문을 돌며 확인
result = 1
value = 1
for i in range(N-1):
    if jewel_red[i] == jewel_red[i+1] or jewel_blue[i] == jewel_blue[i+1]:
        value = 1
        continue
    value += 1
    result = max(result, value)

# 출력부
print(result)