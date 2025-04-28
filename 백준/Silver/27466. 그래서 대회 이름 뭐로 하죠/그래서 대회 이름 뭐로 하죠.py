# 입력부
N, M = map(int, input().split())
S = input()

# 초기값 선언
moeum = ['A', 'E', 'I', 'O', 'U']

# 단어 확인
result_letter = ''
for i in range(M-3, N):
    letter = S[i]
    
    # 단어가 이루어진 현황별 확인
    if result_letter == '':
        if letter != 'A': continue
        result_letter += letter
        continue

    if result_letter == 'A':
        if letter != 'A': continue
        result_letter += letter
        continue

    if result_letter == 'AA':
        if letter in moeum: continue
        result_letter += letter
        continue        

# 결과 계산 및 출력부
result = len(result_letter) == 3
print('YES' if result else 'NO')
if result:
    prefix = S[:M-3]
    print(prefix+result_letter)