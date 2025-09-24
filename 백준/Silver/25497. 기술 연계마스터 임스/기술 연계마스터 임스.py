# 입력부
N = int(input())
command = input()

# 초기값 선언
answer = 0
S_enter = 0
L_enter = 0

# 기술 확인
for combo in command:
    if combo == 'S': S_enter += 1
    elif combo == 'L': L_enter += 1
    elif combo == 'K':
        if S_enter == 0: break
        S_enter -= 1
        answer += 1
    elif combo == 'R':
        if L_enter == 0: break
        L_enter -= 1
        answer += 1
    else: answer += 1

# 출력부
print(answer)