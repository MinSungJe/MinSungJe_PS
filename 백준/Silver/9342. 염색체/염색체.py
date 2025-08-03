# 모듈 불러오기
import re

# 입력부
T = int(input())
genes = [input() for _ in range(T)]

# 유전자 검사
for gene in genes:
    checker = re.compile('^([A-F]?)(A+)(F+)(C+)([A-F]?)$')

    # 정규표현식 확인
    answer = checker.match(gene)
    print('Infected!' if answer else 'Good')