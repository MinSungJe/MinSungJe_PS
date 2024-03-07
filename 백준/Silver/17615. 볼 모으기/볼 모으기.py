# 입력부
N = int(input())
ball = list(input())

# R과 B의 개수 확인
red = 0
blue = 0
for i in range(N):
    if ball[i] == 'R': red += 1
    else: blue += 1

# R 선택(오른쪽으로 이동)
Rcheck1 = 0
Rresult1 = 0
for i in range(N):
    if Rcheck1 == red: break
    if ball[i] == 'R': Rcheck1 += 1
    else: Rresult1 += 1

# R 선택(왼쪽으로 이동)
Rcheck2 = 0
Rresult2 = 0
for i in range(N-1, -1, -1):
    if Rcheck2 == red: break
    if ball[i] == 'R': Rcheck2 += 1
    else: Rresult2 += 1

# B 선택
Bcheck1 = 0
Bresult1 = 0
for i in range(N):
    if Bcheck1 == blue: break
    if ball[i] == 'B': Bcheck1 += 1
    else: Bresult1 += 1

# B 선택(왼쪽으로 이동)
Bcheck2 = 0
Bresult2 = 0
for i in range(N-1, -1, -1):
    if Bcheck2 == blue: break
    if ball[i] == 'B': Bcheck2 += 1
    else: Bresult2 += 1

# 출력부
print(min(Rresult1, Rresult2, Bresult1, Bresult2))