# 입력부
N = int(input())
pages = list(map(int, input().split()))

# 홀수 페이지 수 구하기
answer = 0
for page in pages:
    answer += page // 2 + page % 2

# 출력부
print(answer)