# 입력부
N = int(input())
board = list(map(int, input().split()))

# 칠판에 작성한 내용 기록용 배열 선언
record = [0 for _ in range(51)]

# 기록
for i in range(N): record[board[i]] += 1

# 결과값 도출
result = -1
for i in range(51):
    if i == record[i]: result = i

# 출력부
print(result)