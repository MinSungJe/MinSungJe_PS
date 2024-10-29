# 입력부
N = int(input())

# 초기값 선언
L = 2*N-1
M = L // 2

# 별 찍기
for i in range(L):
    line = ''
    if i == 0 or i == L-1: stamp = '*'*N
    else: stamp = f"*{' '*(N-2)}*"

    if i < M:
        line += ' ' * i
        line += stamp
        line += ' ' * (2*(N-1-i)-1)
        line += stamp
    
    if i == M:
        line += ' ' * i
        line += stamp
        line += ' '*(N-2)
        line += '*'

    if i > M:
        line += ' ' * (2*(N-1)-i)
        line += stamp
        line += ' ' * (2*(i-(N-1))-1)
        line += stamp

    # 출력부
    print(line)