# 입력부
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 살아남을 수 있는 턴 비교
turnA = (A[1] // B[0]) + (1 if A[1] % B[0] > 0 else 0)
turnB = (B[1] // A[0]) + (1 if B[1] % A[0] > 0 else 0)

# 비교
answer = 'DRAW'
if turnA > turnB: answer = 'PLAYER A'
if turnA < turnB: answer = 'PLAYER B'

# 출력부
print(answer)