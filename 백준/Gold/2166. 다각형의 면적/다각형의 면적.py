# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
point = [list(map(int, input().split())) for _ in range(N)]
point.append(point[0])

# 초기값 설정
result = 0
sum1 = 0
sum2 = 0

# 신발끈 공식
# 1. 교차선끼리 곱의 합을 구한다.
for i in range(N):
    sum1 += point[i][0] * point[i+1][1]
    sum2 += point[i][1] * point[i+1][0]

# 2. 합끼리 뺀 뒤 절대값을 취하고 그 값에 1/2을 곱한다.
result = (1/2) * abs(sum1 - sum2)

# 출력부
print(f"{result:.1f}")