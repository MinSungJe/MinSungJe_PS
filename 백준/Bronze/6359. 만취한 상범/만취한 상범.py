# TC
T = int(input())

for _ in range(T):
    # 입력부
    n = int(input())

    # 초기값 선언
    rooms = [0 for _ in range(n+1)]

    # 문 닫기
    for door in range(1, n+1):
        for i in range(door, n+1, door): rooms[i] = 1-rooms[i]
    
    # 출력부
    answer = sum(rooms)
    print(answer)