# 입력부
N = int(input())

# DFS
def DFS(idx, value):
    # 결과 확인
    if idx == N:
        if value % 3 == 0: return 1
        return 0

    # 다음 탐색
    result = 0
    for number in (0, 1, 2):
        result += DFS(idx+1, value*10+number)

    return result

# 함수 호출 및 출력부
result = DFS(1, 1) + DFS(1, 2)
print(result)