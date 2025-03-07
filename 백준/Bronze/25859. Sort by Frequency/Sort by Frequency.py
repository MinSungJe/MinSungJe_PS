# 입력부
letter = input()

# 97 122
# 초기값 선언
letterList = [0 for _ in range(123)]

# 빈도 기록
for l in letter: letterList[ord(l)] += 1

# 가장 높은 빈도부터 확인
result = ''
maxValue = max(letterList[97:123])
while maxValue:
    for i in range(97, 123):
        if letterList[i] == maxValue: result += chr(i) * maxValue
    maxValue -= 1

# 출력부
print(result)