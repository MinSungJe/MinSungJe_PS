# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
predict = [int(input()) for _ in range(N)]

# 예측 정렬
predict.sort()

# 결과값 계산
result = 0
real = 1
for i in range(N):
    result += abs(predict[i]-real)
    real += 1

# 출력부
print(result)