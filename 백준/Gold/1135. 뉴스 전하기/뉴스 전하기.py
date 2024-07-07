# 입력부
N = int(input())
parent = list(map(int, input().split()))

# 그래프 그리기
graph = [list() for _ in range(N)]
for i in range(1, N):
    A, B = i, parent[i]
    graph[B].append(A)

# DP 배열 선언
DP = [0 for _ in range(N)]

# DFS(+DP)
def DFS(node):
    # 메모이제이션
    if DP[node]: return DP[node]

    # 탐색 결과값 모으기
    results = list()
    for node_ in graph[node]:
        results.append(DFS(node_))
    # 자식이 없는 리프노드의 경우 0 투입
    if not results: results.append(0)
    
    # 결과값을 큰 순으로 정렬(그리디)
    results.sort(reverse=True)
    # 전파 시간 확인 -> 전파시간이 긴 부하직원에게 먼저 전달
    time = [results[i]+(i+1) for i in range(len(results))]

    # 가장 긴 시간 도출
    result = max(time)
    DP[node] = result # 메모이제이션
    return result

# 함수 호출 및 출력부
result = DFS(0) - 1
print(result)