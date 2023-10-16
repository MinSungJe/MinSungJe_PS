# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())

# 초기값 선언
INF = 101
graph = [list() for _ in range(N)]
result = [[INF if i != j else 0 for j in range(N)] for i in range(N)]

# 그래프 입력 및 결과배열 수정
for _ in range(M):
    A, B = map(int, input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)
    result[A-1][B-1] = 1
    result[B-1][A-1] = 1

# 플로이드-워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            result[i][j] = min(result[i][j], result[i][k]+result[k][j])

# 출력부
answer = -1
output = 0
for i, ans in enumerate(result):
    if answer == -1 or sum(ans) < answer:
        answer = sum(ans)
        output = i+1 
print(output)