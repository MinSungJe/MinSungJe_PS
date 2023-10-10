# 빠른 입력
import sys
def input(): return sys.stdin.readline().rstrip()

# test_case 구현
T = int(input())
for test_case in range(1,T+1):
    # 초기값 선언
    closet = {}
    result = 1
    
    # 입력부
    n = int(input())
    for _ in range(n):
        Name, Type = input().split()
        if Type in closet.keys(): closet[Type].append(Name)
        else: closet[Type] = [Name]

    # 각 타입마다 옷 개수 세기
    for wear in closet:
        result *= len(closet[wear]) + 1

    # 출력부, 아무것도 입지않은 경우 하나 빼주기
    print(result-1)