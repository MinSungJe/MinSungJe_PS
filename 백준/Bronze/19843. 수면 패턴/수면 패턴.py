# 입력부
T, N = map(int, input().split())

# 주어진 시간을 수치로 변경하는 함수
def getTimeByNumber(day, time):
    result = time
    if day == 'Tue': result += 24
    if day == 'Wed': result += 48
    if day == 'Thu': result += 72
    if day == 'Fri': result += 96

    return result

# 수면시간 체크
sleepTime = 0
for _ in range(N):
    day1, time1, day2, time2 = input().split()
    sleepTime += getTimeByNumber(day2, int(time2)) - getTimeByNumber(day1, int(time1))

# 더 자야하는 시간 체크
result = max(0, T - sleepTime)

# 출력부
print(result if result <= 48 else -1)