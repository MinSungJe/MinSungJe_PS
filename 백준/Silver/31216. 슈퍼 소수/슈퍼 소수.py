# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 에라토스테네스의 체
maximum = 350000
sosu = [1 for _ in range(maximum+1)]
sosu[0] = 0
sosu[1] = 0
for i in range(2, maximum):
    if sosu[i] == 1:
        for j in range(2*i, maximum, i): sosu[j] = 0

# 슈퍼 소수 찾기
super_sosu = [0]
sosu_idx = 0
for i in range(len(sosu)):
    if sosu[i]:
        sosu_idx += 1
        if sosu[sosu_idx]: super_sosu.append(i)

# 입력부
T = int(input())
for _ in range(T):
    n = int(input())

    # 출력부
    print(super_sosu[n])