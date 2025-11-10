# 입력부
N, S = map(int, input().split())
numbers = list(map(int, input().split()))

# 초기값 선언
answer = 0

# DFS
def DFS(idx, value, counts):
    global answer
    # 탐색 종료
    if idx >= N:
        if value == S and counts > 0: answer += 1
        return

    # 다음 탐색
    DFS(idx+1, value+numbers[idx], counts+1)
    DFS(idx+1, value, counts)

# 함수 호출 및 출력부
DFS(0, 0, 0)
print(answer)