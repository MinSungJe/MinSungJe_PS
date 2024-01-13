# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    n, d, c = map(int, input().split())

    # 그래프 그리기
    graph = [list() for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))

    # 초기값 선언
    INF = 10000001
    result = [INF for _ in range(n+1)]
    result[c] = 0
    heap = [(0, c)]

    # 다익스트라 알고리즘
    while heap:
        dist, node = heapq.heappop(heap)

        if dist > result[node]: continue

        for value, node_ in graph[node]:
            dist_ = dist+value

            if dist_ >= result[node_]: continue
            result[node_] = dist_
            heapq.heappush(heap, (dist_, node_))
    
    # 출력부
    answer = [0, 0]
    for i in range(1, n+1):
        if result[i] < INF:
            answer[0] += 1
            answer[1] = max(answer[1], result[i])
    print(*answer)