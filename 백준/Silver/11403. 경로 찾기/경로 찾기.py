# 빠른 입력 및 재귀함수 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
N = int(input())
edge = [list(map(int, input().split())) for _ in range(N)]

# DFS 준비
def DFS(idx):
    global result
    # 탐색 불가 조건 : 이미 탐색한 위치인 경우
    if result[idx] == 1: return

    # 탐색
    result[idx] = 1

    # 다음 탐색
    for next in range(N):
        if edge[idx][next] == 1: DFS(next)

# 첫번째 노드부터 탐색 및 결과 출력
for i in range(N):
    result = [0 for _ in range(N)]
    for next in range(N):
        if edge[i][next] == 1: DFS(next)
    print(*result)