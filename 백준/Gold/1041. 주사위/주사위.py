# 입력부
N = int(input())
A, B, C, D, E, F = map(int, input().split())

# 1면, 2면, 3면들의 배열 및 최솟값 계산
oneFace = min((A,B,C,D,E,F))
twoFace = min(A+B, A+C, A+D, A+E, B+D, D+E, C+E, B+C, B+F, C+F, D+F, E+F)
threeFace = min(A+B+C, A+C+E, A+D+E, A+B+D, B+C+F, B+D+F, C+E+F, D+E+F)

# 실제 N * N * N 값 계산
if N == 1: result = (A+B+C+D+E+F) - max(A,B,C,D,E,F)
else: result = oneFace * (N-2) * (5*N-6) + twoFace * (2*N-3) * 4 + threeFace * 4
print(result)