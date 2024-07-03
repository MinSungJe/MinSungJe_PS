# 재귀 제한 해제
import sys
sys.setrecursionlimit(10**6)

# DFS
def DFS(idx, numbers):
    # 선택 완료
    if idx > S[0]:
        if len(numbers) == 6: print(*numbers) # 출력부
        return
    
    # 탐색 불가 조건
    if len(numbers) > 6: return
    
    # 다음 탐색
    DFS(idx+1, numbers+[S[idx]])
    DFS(idx+1, numbers)

addBlank = False
while True:
    # 입력부
    S = list(map(int, input().split()))
    if not S[0]: break # 입력 종료

    if addBlank: print() # 한줄 띄어쓰기 추가
    DFS(1, []) # 함수호출
    addBlank = True