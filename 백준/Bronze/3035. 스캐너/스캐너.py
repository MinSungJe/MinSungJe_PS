# 입력부
R, C, ZR, ZC = map(int, input().split())
Map = [list(input()) for _ in range(R)]

# 초기값 선언
answer = [['' for _ in range(C * ZC)] for _ in range(R * ZR)]

for x in range(R * ZR):
    for y in range(C * ZC): answer[x][y] = Map[x // ZR][y // ZC]

# 출력부
for row in answer: print(''.join(row))