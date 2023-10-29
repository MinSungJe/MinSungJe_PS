# 빠른 입력 및 모듈 불러오기
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

# 입력부
n = int(input())
m = int(input())

# 초기값 선언
INF = 100000001
graph = [list() for _ in range(n+1)]
result = [INF for _ in range(n+1)]
Way = [list() for _ in range(n+1)]

# 그래프 입력
for _ in range(m):
    S, E, V = map(int, input().split())
    graph[S].append((V, E))

# 출발점과 도착점 입력받기
A, B = map(int, input().split())
result[A] = 0

# 다익스트라
heap = [(0, A, [A])]
while heap:
    dist, current, wayList = heapq.heappop(heap)

    # 탐색 불가 조건 : 현재 거리가 기록된 거리보다 긺
    if dist > result[current]: continue

    # 다음 탐색
    for next in graph[current]:
        V_ = dist + next[0]
        E_ = next[1]

        # 탐색 불가 조건 : 예상 거리가 기록된 거리보다 짧지 않음
        if V_ >= result[E_]: continue

        # 배열 수정
        result[E_] = V_
        Way[E_] = wayList + [E_]

        heapq.heappush(heap, (V_, E_, Way[E_]))

# 출력부
print(result[B])
if Way[B]:
    print(len(Way[B]))
    print(*Way[B])
else:
    print(1)
    print(A)