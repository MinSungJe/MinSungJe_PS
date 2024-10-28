# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
M, N = map(int, input().split())
value = [1 for _ in range(2*M-1)]
for _ in range(N):
    # 0, 1, 2 값 더하기
    zero, one, two = map(int, input().split())
    for i in range(zero, zero+one): value[i] += 1
    for i in range(zero+one, zero+one+two): value[i] += 2

# 출력부
print(' '.join(list(map(str, value[M-1:]))))
for i in range(M-2, -1, -1):
    print(f'{value[i]} ' + ' '.join(list(map(str, value[M:]))))