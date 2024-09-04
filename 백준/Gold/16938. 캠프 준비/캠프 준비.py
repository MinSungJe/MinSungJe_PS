# 입력부
N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))

# 문제 난이도 정렬
A.sort()

# 초기값 선언
INF = 1000001

# DFS
def DFS(idx, visited):
    # 탐색 종료
    if idx == N:
        # 괜찮은 문제인지 확인
        count = 0
        Sum = 0
        min_value = INF
        max_value = 0
        for i in range(N):
            if (visited & 1<<i):
                count += 1
                value = A[i]
                Sum += value
                min_value = min(min_value, value)
                max_value = max(max_value, value)

        # 괜찮지 않음
        if count <= 1: return 0
        if Sum < L or Sum > R: return 0
        gap_value = max_value - min_value
        if gap_value < X: return 0

        return 1
    
    # 다음 탐색
    result = 0
    result += DFS(idx+1, visited|1<<idx)
    result += DFS(idx+1, visited)

    return result

# 함수 호출 및 출력부
result = DFS(0, 0)
print(result)