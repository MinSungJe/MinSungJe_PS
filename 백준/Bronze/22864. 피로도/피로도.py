# 입력부
A, B, C, M = map(int, input().split())

# 초기값 선언
tired = 0
answer = 0

# 시간 별로 확인
for _ in range(24):
    # 일할 수 없으면 쉬기
    if tired + A > M:
        tired = max(0, tired - C)
        continue
    
    # 일하기
    tired += A
    answer += B

# 출력부
print(answer)