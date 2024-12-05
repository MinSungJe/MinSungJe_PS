# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# 입력부
TC = int(input())
for _ in range(TC):
    letter = input()

    # 초기값 선언
    beforeCursor = deque()
    afterCursor = deque()
    
    # 입력한 키 적용
    for cmd in letter:
        if not cmd in ('<', '>', '-'):
            beforeCursor.append(cmd)
            continue

        if cmd == '<' and beforeCursor:
            afterCursor.appendleft(beforeCursor.pop())
        
        if cmd == '>' and afterCursor:
            beforeCursor.append(afterCursor.popleft())

        if cmd == '-' and beforeCursor:
            beforeCursor.pop()
    
    # 출력부
    result = ''.join(list(beforeCursor + afterCursor))
    print(result)