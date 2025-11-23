A, B = map(int, input().split())
C = int(input())

# 분으로 변환
minutes = (A * 60 + B + C) % 1440

# 다시 시로 변환
answer = [minutes // 60, minutes % 60]
print(*answer)