# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# TC
T = int(input())
for test_case in range(1, T+1):
    # 입력부
    N, M = map(int, input().split())
    students = [list(map(int, input().split())) for _ in range(M)]

    # 초기값 선언
    result = 0
    books = [True for _ in range(N+1)]

    # 볼 책이 적은 인원 순으로 정렬
    students.sort(key=lambda x:(x[1], x[0]))

    # 책 제공하기
    for a, b in students:
        for i in range(a, b+1):
            if not books[i]: continue
            books[i] = False
            result += 1
            break
    
    # 출력부
    print(result)