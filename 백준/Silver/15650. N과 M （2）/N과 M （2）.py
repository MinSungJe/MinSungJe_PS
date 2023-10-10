# 입력부
N, M = map(int, input().split())

# 초기값 선언
result = [0 for _ in range(M)]

# DFS 선언
def DFS(idx, limit): # idx: 배열의 몇 번째 수를 채울 것인지, limit: 숫자 제한
    # 결과 담는 배열 불러오기
    global result
    # 배열 출력 조건 : 배열에 값이 모두 채워짐
    if idx == M:
        print(*result)
        return
    
    # 배열에 값 채우기
    for i in range(limit, N+1):
        result[idx] = i
        DFS(idx+1,i+1)

# 출력부
DFS(0,1)