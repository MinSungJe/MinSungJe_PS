# 모듈 불러오기
from itertools import combinations

# 입력부
L, C = map(int, input().split())
letters = list(input().split())

# 자음/모음 구분
ja = list()
mo = list()
for i in range(C):
    if letters[i] in ('a', 'e', 'i', 'o', 'u'): mo.append(letters[i])
    else: ja.append(letters[i])

# 모음 개수 확인
result = list()
for mo_length in range(1, len(mo)+1):
    ja_length = L-mo_length

    if ja_length < 2: continue

    # 단어 구하기
    for mos in combinations(mo, mo_length):
        for jas in combinations(ja, ja_length): result.append(sorted(mos+jas))

# 출력부
for ans in sorted(result): print(''.join(ans))