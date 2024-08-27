# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())
S = int(input())
store = [list(map(int, input().split())) for _ in range(S)]
P = list(map(int, input().split()))

# 둘 사이 최단거리 비교 함수
def dist(pos1, value1, pos2, value2):
    # 시계
    clock_result = 0
    P1, V1, P2, V2 = pos1, value1, pos2, value2

    while True:
        if P1 == 1 or P1 == 4:
            # 도착
            if P1 == P2 and V1 <= V2:
                clock_result += V2 - V1
                break
            
            # 시계 이동
            if P1 == 1:
                clock_result += N - V1
                P1 = 4
                V1 = 0
            else:
                clock_result += M - V1
                P1 = 2
                V1 = N
        
        else:
            # 도착
            if P1 == P2 and V1 >= V2:
                clock_result += V1 - V2
                break

            # 시계 이동
            if P1 == 2:
                clock_result += V1
                P1 = 3
                V1 = M
            else:
                clock_result += V1
                P1 = 1
                V1 = 0

    # 반시계
    not_clock_result = 0
    P1, V1, P2, V2 = pos1, value1, pos2, value2

    while True:
        if P1 == 1 or P1 == 4:
            # 도착
            if P1 == P2 and V1 >= V2:
                not_clock_result += V1 - V2
                break
            
            # 시계 이동
            if P1 == 1:
                not_clock_result += V1
                P1 = 3
                V1 = 0
            else:
                not_clock_result += V1
                P1 = 1
                V1 = N
        
        else:
            # 도착
            if P1 == P2 and V1 <= V2:
                not_clock_result += V2 - V1
                break

            # 시계 이동
            if P1 == 2:
                not_clock_result += N - V1
                P1 = 4
                V1 = M
            else:
                not_clock_result += M - V1
                P1 = 2
                V1 = 0
    
    return min(clock_result, not_clock_result)

# 함수 호출 및 출력부
result = 0
for i in range(S): result += dist(P[0], P[1], store[i][0], store[i][1])
print(result)