# 입력부
E, S, M = map(int, input().split())

# 초기값 설정
result = 1
E_, S_, M_ = 1, 1, 1

# 달력 넘기기
while True:
    # 종료
    if E == E_ and S == S_ and M == M_: break

    result += 1
    E_ += 1
    if E_ > 15: E_ -= 15
    S_ += 1
    if S_ > 28: S_ -= 28
    M_ += 1
    if M_ > 19: M_ -= 19

# 출력부
print(result)