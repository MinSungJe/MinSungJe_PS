# DP 배열 만들기
DP = [0 for _ in range(251)]
DP[0] = 1
DP[1] = 1
DP[2] = 3
for i in range(3, 251):
    DP[i] = DP[i-1]+(2*DP[i-2])

while True:
    try:
        n = int(input()) # 입력부
        print(DP[n]) # 출력부
    except:
        break # 입력 종료