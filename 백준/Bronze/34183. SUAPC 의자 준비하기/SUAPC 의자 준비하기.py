N, M, A, B = map(int, input().split())

chair = 3 * N - M
if chair <= 0: answer = 0
else: answer = chair * A + B
print(answer)