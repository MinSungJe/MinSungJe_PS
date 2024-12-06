# 입력부
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# 숫자 배열 정렬
numbers.sort()

def DFS(idx, result):
    # 출력부
    if idx == M:
        print(*result)
        return
    
    # 다음 탐색
    for i in range(N):
        DFS(idx+1, result+[numbers[i]])

# 함수 호출
DFS(0, [])