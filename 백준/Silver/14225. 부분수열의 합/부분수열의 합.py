# 모듈 불러오기
from itertools import combinations

# 입력부
N = int(input())
S = list(map(int, input().split()))

# 초기값 선언
INF = 2000001
visited = [False for _ in range(INF+1)]

# 조합 구하고 합 기록하기
for length in range(len(S) + 1):
    for numbers in combinations(S, length): visited[sum(numbers)] = True

# 가장 작은 자연수 구하기
answer = INF+1
for i in range(INF+1):
    if visited[i]: continue
    answer = i
    break

# 출력부
print(answer)