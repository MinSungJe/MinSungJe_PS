# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
N = int(input())
students = [float(input()) for _ in range(N)]

# 정렬
students.sort()

# 출력부
for i in range(7): print(f'{students[i]:.3f}')