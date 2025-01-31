# 입력부
N, M = map(int, input().split())
letter = input()

# 알파벳 인덱스 구하기
def getAlphabetIndex(alphabet): return ord(alphabet)-97

# 알파벳 등장 리스트 만들기
alphabet = [0 for _ in range(26)]

# 알파벳 기록
for l in letter: alphabet[getAlphabetIndex(l)] += 1

# 가장 앞서는 문자 제거
idx = 0
while M:
    # 모두 제거
    if alphabet[idx] == 0:
        idx += 1
        continue

    # 알파벳 제거
    alphabet[idx] -= 1
    M -= 1

# 남은 문자열 출력
result = ''
for i in range(N-1, -1, -1):
    l = letter[i]

    # 알파벳이 없다면 continue
    if alphabet[getAlphabetIndex(l)] == 0: continue

    # 있다면 결과에 추가
    alphabet[getAlphabetIndex(l)] -= 1
    result = l + result

# 출력부
print(result)