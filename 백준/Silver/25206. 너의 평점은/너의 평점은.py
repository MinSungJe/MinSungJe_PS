# 초기값 선언
scoreChart = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}
getScore = 0
totalScore = 0


# 입력부
while True:
    try:
        subject, score, grade = input().split()
        if grade == 'P': continue
        getScore += float(score) * scoreChart[grade]
        totalScore += float(score)

    except:
        break

# 출력부
result = getScore / totalScore
print(result)