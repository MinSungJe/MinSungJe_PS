# 입력부
letters = list(input())

# 초기값 선언
visited = [False for _ in range(len(letters))]

# 사전순으로 먼저인지 확인하는 함수
def isFirst(A, B):
    if ord(A) < ord(B): return True
    else: return False

# 출력하는 함수
def printString():
    for i in range(len(letters)):
        if visited[i]: print(letters[i], end='')
    print()

# 재귀
def selectLetter(arr, startIdx):
    # 정복 완료
    if not arr: return

    # 사전순으로 가장 빠른 노드 찾기
    root_idx = -1
    root_value = '['
    for i in range(len(arr)):
        if visited[startIdx+i]: continue
        if isFirst(arr[i], root_value):
            root_idx = i
            root_value = arr[i]
    
    # 탐색
    visited[startIdx + root_idx] = True
    
    # 출력 후 다음탐색
    printString()
    selectLetter(arr[root_idx+1:], startIdx + root_idx+1)
    selectLetter(arr[:root_idx], startIdx)

# 함수 호출
selectLetter(letters, 0)