# 입력부
plates = input()

# 초기값 선언
prev = ''
answer = 0

# 그릇 높이 확인
for plate in plates:
    if prev != plate: answer += 10
    else: answer += 5
    prev = plate

# 출력부
print(answer)