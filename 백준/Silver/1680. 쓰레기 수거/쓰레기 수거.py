# 빠른 입력 및 모듈 불러오기
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

# TC
T = int(input())
for _ in range(T):
    # 입력부
    W, N = map(int, input().split())
    
    # 초기값 선언
    result = 0
    current = 0
    position = 0

    # 쓰레기차 이동
    for _ in range(N):
        x, w = map(int, input().split())

        # 다음 지역으로 쓰레기차 이동
        result += x - position
        position = x

        # 쓰레기를 실었을 때 쓰레기차의 용량을 넘게 됨
        if current + w > W:
            result += position * 2
            current = 0
        
        # 쓰레기 싣기
        current += w

        # 쓰레기차 꽉 찼는지 확인
        if current == W:
            result += position
            position = 0
            current = 0
    
    # 쓰레기차 돌아오기
    result += position

    # 출력부
    print(result)