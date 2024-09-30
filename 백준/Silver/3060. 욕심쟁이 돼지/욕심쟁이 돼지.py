# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# TC
T = int(input())
for _ in range(T):
    N = int(input())
    pigs = list(map(int, input().split()))

    # 일수 찾기
    result = 1
    while True:
        # 여물이 남아있는지 비교
        value = sum(pigs)
        if value > N: break

        # 하루가 지남
        result += 1

        # 돼지 식탐 추가
        new_pigs = [0, 0, 0, 0, 0, 0]
        for i in range(6): new_pigs[i] = pigs[i] + pigs[(i+1)%6] + pigs[(i+5)%6] + pigs[(i+3)%6]
        for i in range(6): pigs[i] = new_pigs[i]

    # 출력부
    print(result)