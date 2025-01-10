# 입력부
N, M, a, K = map(int, input().split())

# 결과값 계산
rest_people = a-K
max_rank = min(N-1, rest_people) + 1
min_rank = (rest_people // M) + (1 if rest_people % M else 0) + 1

# 출력부
print(max_rank, min_rank)