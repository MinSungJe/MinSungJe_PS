# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
friend = [list() for _ in range(N**2+1)]
turn = list()
for _ in range(N**2):
    temp = list(map(int, input().split()))
    idx = temp[0]
    data = set(temp[1:])
    turn.append(idx)
    friend[idx].append(data)

# 초기값 선언
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
Map = [[0 for _ in range(N)] for _ in range(N)]

# 적절한 자리 찾는 함수
def find_seat(number):
    # 초기값 선언
    X, Y = 0, 0
    friendly, blank = -1, -1
    friend_set = friend[number][0]

    # 탐색 시작
    for x in range(N):
        for y in range(N):
            # 이미 자리가 있음
            if Map[x][y]: continue

            # 자리 점수 매기기
            friendly_, blank_ = 0, 0
            for i in range(4):
                x_, y_ = x+dx[i], y+dy[i]
                # 탐색 불가 조건
                if x_ < 0 or x_ >= N or y_ < 0 or y_ >= N: continue
                
                # 점수 추가
                if Map[x_][y_] == 0: blank_ += 1
                if {Map[x_][y_]}.intersection(friend_set): friendly_ += 1
            
            # 점수 비교 후 넘기기
            if friendly_ < friendly: continue
            if friendly_ == friendly and blank_ <= blank: continue

            # 자리 반영
            friendly = friendly_
            blank = blank_
            X, Y = x, y
    
    # 자리 앉히기
    Map[X][Y] = number

# 모든 학생 자리 앉히기
for student in turn: find_seat(student)

# 만족도 확인
result = 0
for X in range(N):
    for Y in range(N):
        # 초기값 선언
        temp = 0
        student = Map[X][Y]

        # 4방향 탐색
        for i in range(4):
            X_, Y_ = X+dx[i], Y+dy[i]
            
            # 탐색 불가 조건
            if X_ < 0 or X_ >= N or Y_ < 0 or Y_ >= N: continue

            # 값 계산
            if {Map[X_][Y_]}.intersection(friend[student][0]): temp += 1

        # 만족도 계산
        result += int(10 ** (temp-1))

# 출력부
print(result)