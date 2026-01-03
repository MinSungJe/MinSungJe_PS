# TC
N = int(input())

# 초기값 선언
answer = [0, 0]

for _ in range(N):
    # 입력부
    A, B = map(int, input().split())

    # 값 추가하기
    if A > B: answer[0] += 1
    if A < B: answer[1] += 1

# 출력부
print(*answer)