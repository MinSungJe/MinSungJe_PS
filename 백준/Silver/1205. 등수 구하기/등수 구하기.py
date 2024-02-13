# 초기값 선언
result = 1

# 입력부
N, score, P = map(int, input().split())
if N:
    rank = list(map(int, input().split()))

    # 순위 확인
    rank.sort(reverse=True)
    for i in range(N):
        if rank[i] > score:
            result += 1
        
    if N >= P and score <= rank[P-1]: result = -1

# 출력부
print(result if result <= P else -1)