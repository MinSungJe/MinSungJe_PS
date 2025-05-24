# 입력부
Map = [list(input()) for _ in range(8)]

# 하얀칸 확인
result = 0
for x in range(8):
    for y in range(8):
        # 검은칸인 경우 넘어가기
        if (x+y) % 2 != 0: continue

        # 말이 있는 경우 세기
        if Map[x][y] == 'F': result += 1

# 출력부
print(result)