# 입력부
N = int(input())
A = input().split()
B = input().split()

# 파트너 자료구조 생성
partner = dict()
for i in range(N): partner[A[i]] = B[i]

# 결과 확인
result = 'good'
for k, v in partner.items():
    if k == v: result = 'bad'
    if k != partner[v]: result = 'bad'

# 출력부
print(result)