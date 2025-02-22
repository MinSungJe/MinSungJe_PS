# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 일반쓰레기인지 확인하는 함수
def checkMixed(letter):
    return len(set(list(letter))) > 1

# 입력부
N = int(input())
trashes = list(input() for _ in range(N))
P, C, V, S, G, F = map(int, input().split())
O = int(input())

# 초기값 선언
result = 0
cost = {
    "P": P,
    "C": C,
    "V": V,
    "S": S,
    "G": G,
    "F": F,
    "O": O,
}

# 쓰레기 분리배출 시작
for trash in trashes:
    L = len(trash)
    # 일반쓰레기
    if checkMixed(trash):
        result += O * L
        continue

    # 분리배출 쓰레기(일반 쓰레기로도 버릴 수 있음)
    trashType = trash[0]
    result += min(cost[trashType] * L, O * L)

# 출력부
print(result)