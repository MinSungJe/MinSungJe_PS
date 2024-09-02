# 입력부
X, Y = map(int, input().split())

# 초기값 선언
gap = Y - X

# 함수 선언
def solution(gap):
    if gap == 0: return 0

    result = 0
    value = 0
    idx = 1
    while True:
        value += idx
        result += 1
        if value >= gap: break
        value += idx
        result += 1
        if value >= gap: break

        idx += 1

    return result

# 함수 호출 및 출력부
print(solution(gap))