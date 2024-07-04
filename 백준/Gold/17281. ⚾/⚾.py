# 빠른 입력 및 모듈 불러오기
from itertools import permutations
import sys
def input(): return sys.stdin.readline().rstrip()

# 야구게임
def baseball(Order):
    # 초기값 선언
    time = 1 # 이닝
    out = 0 # 아웃카운트
    first, second, third = False, False, False # 주자
    turn = 0 # 주자 순서
    score = 0 # 점수

    # 게임 진행
    while time <= N:
        # 순서 진행
        value = hitter[time-1][Order[turn]]
        if value == 1: # 안타
            if third:
                third = False
                score += 1
            if second:
                third = True
                second = False
            if first:
                second = True
                first = False
            first = True

        if value == 2: # 2루타
            if third:
                third = False
                score += 1
            if second:
                second = False
                score += 1
            if first:
                third = True
                first = False
            second = True

        if value == 3: # 3루타
            if third:
                third = False
                score += 1
            if second:
                second = False
                score += 1
            if first:
                first = False
                score += 1
            third = True

        if value == 4: # 홈런
            if third:
                third = False
                score += 1
            if second:
                second = False
                score += 1
            if first:
                first = False
                score += 1
            score += 1

        if value == 0: out += 1 # 아웃

        # 다음 타자
        turn = (turn+1)%9

        # 3아웃
        if out == 3:
            # 변수 초기화
            first, second, third, out = False, False, False, 0
            # 이닝 추가
            time += 1

    return score

# 입력부
N = int(input())
hitter = [list(map(int, input().split())) for _ in range(N)]

# 함수 호출
result = 0
for order in permutations(list(range(9)), 9):
    if order[3] != 0: continue # 4번타자 고정
    value = baseball(order)
    result = max(result, value)

# 출력부
print(result)