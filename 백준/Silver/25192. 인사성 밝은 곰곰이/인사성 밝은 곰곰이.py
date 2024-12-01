# 입력부
N = int(input())

# 초기값 선언
result = 0
gomgomed = set()

for _ in range(N):
    letter = input()

    # 새로 들어왔는지 확인
    if letter == 'ENTER':
        gomgomed = set()
        continue

    # 이미 곰곰티콘을 사용한 인원임
    if gomgomed.intersection(set([letter])): continue
    
    # 곰곰티콘 사용
    result += 1
    gomgomed.add(letter)

# 출력부
print(result)