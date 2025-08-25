# 입력부
A, B = input().split()

# 이상한 곱셈 계산
answer = 0
A_numbers = list(map(int, list(A)))
B_numbers = list(map(int, list(B)))

for a in A_numbers:
    for b in B_numbers: answer += a * b

# 출력부
print(answer)