# 입력부
N = int(input())
F = int(input())

# 백의자리 이상 값 추출
rest = N - (N % 100)

# 뒷 두자리 확인
answer = 0
for i in range(100):
    if (rest + i) % F == 0:
        answer = i
        break

# 출력부
print(f"{answer:02}")