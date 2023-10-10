# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
M = int(input())

# 초기값 선언
S = set()

# 명령어 입력 및 출력
for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'add':
        if not cmd[1] in S: S.add(cmd[1])

    if cmd[0] == 'remove':
        if cmd[1] in S: S.discard(cmd[1])

    if cmd[0] == 'check':
        if cmd[1] in S: print(1)
        else: print(0)

    if cmd[0] == 'toggle':
        if cmd[1] in S: S.discard(cmd[1])
        else: S.add(cmd[1])

    if cmd[0] == 'all':
        S = set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])

    if cmd[0] == 'empty':
        S = set()