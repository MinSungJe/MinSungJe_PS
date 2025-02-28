# 입력부
father = input().split()
mother = input().split()

# 색깔 통합
united = list(set(father + mother))

# 앵무새 색 구하기
result = list()
for head in united:
    for tail in united:
        result.append(f"{head} {tail}")

# 중복 제거 후 정렬
result = list(set(result))
result.sort()

# 출력부
for r in result: print(r)