# 입력부
ISBN = input()

# 나머지 계산
result = 0
value = -1
for i in range(10, 0, -1):
    digit = ISBN[10-i]
    if digit == '?':
        value = i
        continue
    
    if digit == 'X':
        result += 10 * i
        continue

    result += int(digit) * i

# 출력부
answer = -1
for i in range(10):
    if (result + i*value) % 11 == 0:
        answer = i
        break
if value == 1 and (result+10) % 11 == 0: answer = 'X'
print(answer)