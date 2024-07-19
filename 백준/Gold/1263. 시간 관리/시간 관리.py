# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]

# 마감 기한 나중 순으로 정렬
tasks.sort(key=lambda x:-x[1])

# 하나씩 일 끝내보기
result = tasks[0][1]
for i in range(N):
    T, S = tasks[i][0], tasks[i][1]

    # 마감기한 확인해서 최대한 미루기
    if S < result: result = S
    result -= T # 일하기

# 출력부
print(max(result, -1))