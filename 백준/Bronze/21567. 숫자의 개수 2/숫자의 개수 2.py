# 입력부
A = int(input())
B = int(input())
C = int(input())
number = A * B * C

# 결과 확인
answer = [0 for _ in range(10)]
for letter in str(number): answer[int(letter)] += 1

# 출력부
for i in range(10): print(answer[i])