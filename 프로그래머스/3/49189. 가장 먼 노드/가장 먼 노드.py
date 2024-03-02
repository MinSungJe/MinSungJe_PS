import heapq

def solution(n, edge):
    answer = 0
    
    INF = 50001
    graph = [list() for _ in range(n+1)]
    result = [INF for _ in range(n+1)]
    result[1] = 0
    
    for A, B in edge:
        graph[A].append(B)
        graph[B].append(A)
    
    heap = [(0, 1)]
    
    while heap:
        dist, node = heapq.heappop(heap)
        if dist > result[node]: continue
        
        for node_ in graph[node]:
            dist_ = dist+1
            if dist_ >= result[node_]: continue
            
            result[node_] = dist_
            heapq.heappush(heap, (dist_, node_))
    
    max_value = 0
    for i in range(1, n+1):
        if result[i] == INF: continue
        max_value = max(max_value, result[i])
    for i in range(1, n+1):
        if max_value == result[i]: answer += 1
    
    return answer