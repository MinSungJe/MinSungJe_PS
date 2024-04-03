# 빠른 입력 및 재귀 제한 해제
import sys
def input(): return sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

# 입력부
numbers = list()
while True:
    try: numbers.append(int(input()))
    except: break

# 재귀
def DFS(numlist):
    # 초기값 선언
    N = len(numlist)
    node = numlist[0]

    # 왼쪽 오른쪽 구별
    left = list()
    right = list()
    for i in range(1, N):
        if node > numlist[i]: left.append(numlist[i])
        else: right.append(numlist[i])
    
    # 후위 순회 및 출력부
    if left: DFS(left)
    if right: DFS(right)
    print(node)

# 함수 호출
DFS(numbers)