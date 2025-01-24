# 입력부
R, B = map(int, input().split())

# 타일 정보 구하기
tiles = R+B

# L, W 구하기
for W in range(1, tiles+1):
    if tiles % W != 0: continue
    L = tiles // W

    # 조건에 맞는 경우 확인
    if (L-2) * (W-2) == B:
        break

# 출력부
print(L, W)