# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N, M = map(int, input().split())

# 초기값 선언
answer = [0 for _ in range(N+1)]

# 친구 확인
for _ in range(M):
    A, B = map(int, input().split())
    answer[A] += 1
    answer[B] += 1

# 출력부
for i in range(1, N+1): print(answer[i])