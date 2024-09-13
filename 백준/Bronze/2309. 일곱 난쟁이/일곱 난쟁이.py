# 모듈 불러오기
from itertools import combinations

# 입력부
height = list(int(input()) for _ in range(9))

# 합이 100인 경우 구하기
for seven_height in combinations(height, 7):
    if sum(seven_height) == 100:
        result = list(seven_height)
        break

# 출력부
result.sort()
for i in range(7): print(result[i])