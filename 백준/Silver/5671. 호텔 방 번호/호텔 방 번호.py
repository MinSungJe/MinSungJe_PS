# 불운이 찾아오는 방 확인
def check_room(number):
    return len(str(number)) == len(set(list(str(number))))

# EOF 입력부
while True:
    try:
        start, end = map(int, input().split())
        # 방 번호 계산
        result = 0
        for room_number in range(start, end+1):
            if check_room(room_number): result += 1

        # 출력부
        print(result)
    except: break