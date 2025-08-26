# 입력부
x, y = map(int, input().split())

# 초기값 선언
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 일자 확인
day = 0
for month in range(x-1): day += days[month]
day += y-1

# 출력부
answer = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'][day % 7]
print(answer)