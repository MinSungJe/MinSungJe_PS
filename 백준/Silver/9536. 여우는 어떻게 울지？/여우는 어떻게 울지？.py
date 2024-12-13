# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
T = int(input())
for test_case in range(1, T+1):
    hawling = input().split()
    record = list()

    while True:
        cmd = input()

        # 종료
        if cmd == 'what does the fox say?': break

        # 각 동물의 울음소리 기록
        record.append(cmd.split()[2])

    # 출력부
    for hawl in hawling:
        if not hawl in record: print(hawl, end=' ')