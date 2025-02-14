# 입력부
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 점수 내기
resultA = 0
resultB = 0
winner = 'D'
for i in range(10):
    if A[i] > B[i]:
        resultA += 3
        winner = 'A'
    if A[i] < B[i]:
        resultB += 3
        winner = 'B'
    if A[i] == B[i]:
        resultA += 1
        resultB += 1

# 승점 확인
if resultA > resultB: winner = 'A'
if resultA < resultB: winner = 'B'

# 출력부
print(resultA, resultB)
print(winner) 