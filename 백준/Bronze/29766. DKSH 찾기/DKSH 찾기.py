# 입력부
letter = input()

# 확인
answer = 0
for i in range(0, len(letter)-3):
    if letter[i:i+4] == 'DKSH': answer += 1

# 출력부
print(answer)