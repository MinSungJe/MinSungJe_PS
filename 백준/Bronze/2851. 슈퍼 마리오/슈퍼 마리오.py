# 입력부
mushes = [int(input()) for _ in range(10)]

# 버섯 더하기
answer = 0
for i in range(10):
    answer += mushes[i]
    if answer >= 100:
        if answer - 100 > 100 - (answer-mushes[i]): answer = answer - mushes[i]
        break

# 출력부
print(answer)