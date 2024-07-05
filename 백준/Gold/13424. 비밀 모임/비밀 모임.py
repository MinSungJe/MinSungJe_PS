# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    N, M = map(int, input().split())

    # 초기값 선언
    INF = 100001
    distance = [[INF if i != j else 0 for j in range(N+1)] for i in range(N+1)]
    # 그래프 값 반영
    for _ in range(M):
        a, b, c = map(int, input().split())
        distance[a][b] = c
        distance[b][a] = c

    # 플로이드 워셜 알고리즘
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

    # 친구가 있는 위치 확인
    K = int(input())
    friends = list(map(int, input().split()))

    # 결과값 도출
    result = 0
    min_value = INF * 100
    for destination in range(N, 0, -1): # 목적지 지정
        value = 0
        for friend in friends:
            value += distance[friend][destination]
        if value <= min_value:
            min_value = value
            result = destination
    
    # 출력부
    print(result)