# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# union-find
def find(A):
    if P[A] == A: return A
    P[A] = find(P[A])
    return P[A]

def union(A, B):
    X, Y = find(A), find(B)
    if X == Y: return
    if X < Y: P[Y] = X
    else: P[X] = Y

# TC
while True:
    m, n = map(int, input().split())
    if not m and not n: break # 종료

    # 모든 간선 넣기
    road = [list(map(int, input().split())) for _ in range(n)]
    road.sort(key=lambda x:x[2]) # 간선 길이 기준으로 정렬

    # 초기값 선언
    P = [i for i in range(m)]

    # 모든 간선을 돌아보며 확인(크루스칼 알고리즘)
    result = 0
    for x, y, z in road:
        result += z # 원래 비용 계산
        if find(x) == find(y): continue
        result -= z # 불 켜두기
        union(x, y)

    # 출력부
    print(result)