# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 출력형식 정하는 함수
def outFormat(list):
    if list: return '['+','.join(list)+']'
    else: return '[]'

# 리스트 값 반전하는 함수
def reverseList(list):
    for i in range(0,len(list)//2):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp

    return list

# test_case
T = int(input())
for test_case in range(1,T+1):
    # 입력부
    cmdList = input()
    n = int(input())
    List = deque(input().strip('[]').split(','))
    if n == 0: List = deque()
    
    # 초기값 선언
    isReversed = False
    isError = False

    for cmd in cmdList:
        if cmd == 'R': # R이면 Bool값 Toggle
            if isReversed: isReversed = False
            else: isReversed = True

        if cmd == 'D':
            if not List: # 에러 확인
                isError = True
                break
            else:
                if isReversed: List.pop()
                else: List.popleft()
    
    # 출력부
    if isError: print("error")
    else:
        if isReversed: print(outFormat(reverseList(list(List))))
        else: print(outFormat(list(List)))