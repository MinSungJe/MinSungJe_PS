# 입력부
N, K = map(int, input().split())

# 초기값 선언
hour, minute, second = 0, 0, 0

# 값 구하기
answer = 0
while True:
    if hour == N+1 and minute == 0 and second == 0: break
    
    # K 확인
    result = False
    for check_number in (hour, minute, second):
        number_list = list(str(check_number))
        if len(number_list) == 1: number_list.append('0')
        if str(K) in number_list: result = True

    # 값 더하기
    if result: answer += 1
    
    # 1초 더하기
    second += 1
    if second >= 60:
        minute += 1
        second = 0
    if minute >= 60:
        hour += 1
        minute = 0

# 출력부
print(answer)