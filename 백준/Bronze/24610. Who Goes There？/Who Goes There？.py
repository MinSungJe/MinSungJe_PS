# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
n, m = map(int, input().split())
t = [int(input()) for _ in range(m)]

# 초기값 선언
result = [0 for _ in range(m)]

# 참가권한 나눠주기
while n > 0 and sum(t) > 0:
    for i in range(m):
        if t[i] == 0: continue
        t[i] -= 1
        result[i] += 1

        # 팀 정원 초과
        n -= 1
        if n == 0: break

# 출력부
for r in result: print(r)