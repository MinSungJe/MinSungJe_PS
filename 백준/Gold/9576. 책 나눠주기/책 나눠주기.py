# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 이분매칭 알고리즘
def binaryMatching(idx):
    if visited[idx]: return False
    visited[idx] = True

    a, b = students[idx]

    for i in range(a, b+1):
        target = books[i]
        if target == -1:
            books[i] = idx
            return True
        if binaryMatching(target):
            books[i] = idx
            return True
        
    return False

# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    N, M = map(int, input().split())
    students = [list(map(int, input().split())) for _ in range(M)]

    # 초기값 선언
    result = 0
    books = [-1 for _ in range(N+1)]

    for i in range(M):
        visited = [False for _ in range(M)]
        if binaryMatching(i): result += 1
    
    # 출력부
    print(result)