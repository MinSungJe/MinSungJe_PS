# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, K = map(int, input().split())
lecture = [list(map(int, input().split())) for _ in range(N)]

# 뽑을 역량 별로 최댓갑 구하기
result = 0
for A, B in ((0, 1), (0, 2), (1, 2)):
    lecture.sort(key=lambda x: -(x[A]+x[B]))

    value = 0
    for i in range(K): value += lecture[i][A] + lecture[i][B]
    result = max(result, value)

# 출력부
print(result)