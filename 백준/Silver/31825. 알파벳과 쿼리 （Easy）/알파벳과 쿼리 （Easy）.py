# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 알파벳 묶음 구하는 함수
def getSetOfAlphabet(letter):
    prev = 0
    result = 0
    for i in range(len(letter)):
        if ord(letter[i]) == prev: continue
        result += 1
        prev = ord(letter[i])

    return result

# 새로운 문자 만들기
def createNewLetter(letter, l, r):
    result = ''
    for i in range(len(letter)):
        value = ord(letter[i])
        if i >= l-1 and i < r:
            value += 1
            if value > 90: value = 65
        result += chr(value)

    return result

# 입력부
N, Q = map(int, input().split())
S = input()

# 쿼리별 명령 실행
for _ in range(Q):
    cmd, l, r = map(int, input().split())

    if cmd == 1:
        print(getSetOfAlphabet(S[l-1:r])) # 출력부

    if cmd == 2:
        S = createNewLetter(S, l, r)