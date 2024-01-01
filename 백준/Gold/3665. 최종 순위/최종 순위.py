# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# TC
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    t = list(map(int, input().split()))
    m = int(input())
    cmd = [list(map(int, input().split())) for _ in range(m)]

    # 그래프 그리기
    graph = [set() for _ in range(n+1)]
    level = [0 for _ in range(n+1)]
    for i in range(n):
        A = t[i]
        for j in range(i+1, n):
            B = t[j]
            graph[A].add(B)
            level[B] += 1

    # 그래프 간선 순서 뒤바꾸기
    for a, b in cmd:
        if graph[a].intersection(set([b])):
            graph[a].remove(b)
            graph[b].add(a)
            level[a] += 1
            level[b] -= 1
        elif graph[b].intersection(set([a])):
            graph[b].remove(a)
            graph[a].add(b)
            level[a] -= 1
            level[b] += 1

    # 초기값 선언
    result = []
    Question = False

    # 위상정렬 시작값 넣기
    queue = deque()
    for i in range(1, n+1):
        if not level[i]: queue.append(i)

    # 위상정렬
    while (queue and not Question):
        node = queue.popleft()

        # 탐색
        result.append(node)

        # 다음 탐색
        QuestionCount = 0
        for node_ in graph[node]:
            level[node_] -= 1
            if not level[node_]:
                QuestionCount += 1
                queue.append(node_)

        # 한번에 두 개 이상의 값을 넣음 : 순위 불분명
        if QuestionCount > 1: Question = True

    # 출력부
    if len(result) != n: print("IMPOSSIBLE") # 모든 노드를 탐색하지 못함
    elif Question: print('?')
    else: print(*result)