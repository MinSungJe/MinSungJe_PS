# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# 가위바위보 함수
def getRSPWinner(rspList):
    rspTypeList = list(set(rspList))
    rspTypeLength = len(rspTypeList)

    # 무승부
    if rspTypeLength == 1 or rspTypeLength == 3: return 'N'

    # 승부 내기
    winner = 'R'
    if 'R' in rspTypeList and 'P' in rspTypeList: winner = 'P'
    if 'P' in rspTypeList and 'S' in rspTypeList: winner = 'S'

    return winner
    

# TC
T = int(input())
for _ in range(T):
    # 입력부
    N = int(input())
    robots = [list(input()) for _ in range(N)]
    k = len(robots[0])

    # 초기값 선언
    survived = [1 for _ in range(N)]

    # 가위바위보 진행
    for i in range(k):
        # 이긴 심볼 찾기
        rspList = list()
        for robotIdx in range(N):
            if not survived[robotIdx]: continue
            rspList.append(robots[robotIdx][i])
        winSymbol = getRSPWinner(rspList)

        # 무승부 넘기기
        if winSymbol == 'N': continue

        # 결과 기록
        for robotIdx in range(N):
            if not survived[robotIdx]: continue
            if robots[robotIdx][i] != winSymbol: survived[robotIdx] = 0
    
    # 승자가 가려졌는지 확인 및 출력부
    if sum(survived) == 1:
        for i in range(N):
            if survived[i]: print(i+1)
    else: print(0)