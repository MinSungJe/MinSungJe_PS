# 입력부
P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))
P3 = list(map(int, input().split()))

# CCW 계산
temp = P1[0]*P2[1] + P2[0]*P3[1] + P3[0]*P1[1]
temp -= P1[1]*P2[0] + P2[1]*P3[0] + P3[1]*P1[0]

# 출력부
if temp > 0: print(1)
if temp == 0: print(0)
if temp < 0: print(-1)