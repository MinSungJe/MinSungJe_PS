# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())
m = int(input())

# 초기값 선언
INF = 10000001
result = [[INF if i != j else 0 for j in range(n+1)] for i in range(n+1)]
prev_node = [[-1 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if result[a][b] > c:
        result[a][b] = c
        prev_node[a][b] = a

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            value = result[i][k]+result[k][j]
            if result[i][j] > value:
                result[i][j] = value
                prev_node[i][j] = prev_node[k][j]

# 경로 역추적
path_list = list()
for start in range(1, n+1):
    for end in range(1, n+1):
        # 출력 불가 조건
        if start == end or result[start][end] == INF:
            path_list.append(0)
            continue

        path = [end]
        node = end
        while node != start:
            node = prev_node[start][node]
            path.append(node)
        path_list.append(path[::-1])

# 출력부 1: 플로이드 워셜 결과 출력
for i in range(1, n+1):
    row = list()
    for j in range(1, n+1):
        if result[i][j] == INF: row.append(0)
        else: row.append(result[i][j])
    print(*row)

# 출력부 2: 경로 출력
for p in path_list:
    if not p: print(p)
    else:
        print(len(p), *p)