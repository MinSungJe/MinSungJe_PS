# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    K, M, P = map(int, input().split())

    # 초기값 선언
    phase = [0 for _ in range(M+1)]
    river = [list() for _ in range(M+1)]
    result = [0 for _ in range(M+1)]

    # 그래프 입력받기
    graph = [list() for _ in range(M+1)]
    for _ in range(P):
        A, B = map(int, input().split())
        graph[A].append(B)
        phase[B] += 1
    
    # 위상이 0인 노드(강의 근원)부터 탐색 시작
    heap = list()
    for i in range(1, M+1):
        if phase[i] == 0:
            heapq.heappush(heap, (1, i))
            result[i] = 1

    # 위상 정렬
    while heap:
        value, node = heapq.heappop(heap)

        # 다음 노드 확인
        for node_ in graph[node]:
            phase[node_] -= 1

            # 흐름 값 입력하기
            river[node_].append(value)

            # Strahler 계산 후 다음 탐색
            if phase[node_] == 0:
                max_value = max(river[node_])
                final_value = max_value
                count = 0
                for i in range(len(river[node_])):
                    if river[node_][i] == max_value: count += 1
                    if count > 1: break
                if count >= 2: final_value += 1
                result[node_] = final_value
                heapq.heappush(heap, (final_value, node_))
    
    # 출력부
    print(K, result[M])