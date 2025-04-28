# 입력부
N, M = map(int, input().split())
S = input()

# 초기값 선언
moeum = ['A', 'E', 'I', 'O', 'U']

# 단어 확인
result = 0
for letter in S:
    if result == 0:
        if letter != 'A': continue
        result += 1
        continue

    if result == 1:
        if letter != 'A': continue
        result += 1
        continue
    
    if result == 2:
        if letter in moeum: continue
        result += 1
        continue

# 출력부
print('YES' if result == 3 else 'NO')
if result == 3: print('AAC')