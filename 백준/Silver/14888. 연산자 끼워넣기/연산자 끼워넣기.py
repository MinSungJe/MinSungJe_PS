# 입력부
N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))

INF = 1000000001

# DFS 탐색
def DFS(number, order):
    if order == N: return [number, number]

    # 초기값 선언
    max_result = -INF
    min_result = INF

    # 다음 탐색
    for i in range(4):
        if not operator[i]: continue

        values = list()

        operator[i] -= 1
        if i == 0: values = DFS(number+A[order], order+1)
        if i == 1: values = DFS(number-A[order], order+1)
        if i == 2: values = DFS(number*A[order], order+1)
        if i == 3:
            if number < 0:
                values = DFS(-((-number)//A[order]), order+1)
            else:
                values = DFS(number//A[order], order+1)
        
        max_result = max(max_result, values[0])
        min_result = min(min_result, values[1])

        operator[i] += 1 # backtracking
    
    return [max_result, min_result]
    
# 함수 호출 및 출력부
result = DFS(A[0], 1)
print(*result)