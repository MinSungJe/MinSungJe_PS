# 입력부
N = int(input())
W = list(map(int, input().split()))

# DFS
def DFS(weight):
    # 종료 조건
    n = len(weight)
    if n == 2: return 0

    # 다음 탐색
    result = 0
    for i in range(1, n-1):
        # 배열 만들기
        temp = weight[:i] + weight[i+1:]
        result = max(result, (weight[i-1]*weight[i+1])+DFS(temp))

    return result

# 함수 호출 및 출력부
result = DFS(W)
print(result)